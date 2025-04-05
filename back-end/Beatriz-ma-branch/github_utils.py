import os
from typing import Dict
from fastapi import HTTPException
import requests
from dotenv import load_dotenv
from datetime import datetime
from models_github import GithubStats, LinguagemStats, RepoRequest
from fpdf import FPDF


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


#Estatísticas do USUÁRIO


def buscar_estatisticas(usuario: str) -> GithubStats:
    user_url = f"https://api.github.com/users/{usuario}"
    repos_url = f"https://api.github.com/users/{usuario}/repos?per_page=100"

    user_resp = requests.get(user_url, headers=HEADERS)
    repos_resp = requests.get(repos_url, headers=HEADERS)

    user = user_resp.json()
    repos = repos_resp.json()

    total_commits = 0
    total_branches = 0
    total_stars = 0
    total_forks = 0
    total_prs_open = 0
    total_prs_closed = 0
    total_linguagens = {}

    owner = usuario

    # Verificar se a resposta dos repositórios é válida
    if not isinstance(repos, list):
        print("Erro ao buscar repositórios:", repos_resp.status_code, repos)
        return GithubStats(
            nome=user.get("name", "N/A"),
            login=user.get("login", "N/A"),
            localizacao=user.get("location", "N/A"),
            criado_em=datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime('%d/%m/%Y'),
            seguidores=user.get("followers", 0),
            public_repos=user.get("public_repos", 0),
            commits=0,
            prs_abertas=0,
            prs_fechadas=0,
            branches=0,
            estrelas=0,
            forks=0,
            linguagens=[],
            avatar_url=user.get("avatar_url", "")
        )

    for repo in repos:
        repo_name = repo["name"]
    
        # Commits (até 100)
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?per_page=100"
        commits_resp = requests.get(commits_url, headers=HEADERS)
        if commits_resp.status_code == 200:
            total_commits += len(commits_resp.json())

        # Branches
        branches_url = f"https://api.github.com/repos/{owner}/{repo_name}/branches?per_page=100"
        branches_resp = requests.get(branches_url, headers=HEADERS)
        if branches_resp.status_code == 200:
            total_branches += len(branches_resp.json())

        # PRs abertas
        prs_open_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=open&per_page=100"
        prs_open_resp = requests.get(prs_open_url, headers=HEADERS)
        if prs_open_resp.status_code == 200:
            total_prs_open += len(prs_open_resp.json())

        # PRs fechadas
        prs_closed_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=closed&per_page=100"
        prs_closed_resp = requests.get(prs_closed_url, headers=HEADERS)
        if prs_closed_resp.status_code == 200:
            total_prs_closed += len(prs_closed_resp.json())

        total_stars += repo.get("stargazers_count", 0)
        total_forks += repo.get("forks_count", 0)

        # Linguagens
        lang_url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
        lang_resp = requests.get(lang_url, headers=HEADERS)
        if lang_resp.status_code == 200:
            for lang, qtd in lang_resp.json().items():
                total_linguagens[lang] = total_linguagens.get(lang, 0) + qtd

    # Linguagens em %
    soma_total = sum(total_linguagens.values())
    linguagens = [
        LinguagemStats(linguagem=lang, porcentagem=(qtd / soma_total) * 100)
        for lang, qtd in sorted(total_linguagens.items(), key=lambda x: x[1], reverse=True)[:5]
    ]

    return GithubStats(
        nome=user.get("name", "N/A"),
        login=user.get("login", "N/A"),
        localizacao=user.get("location", "N/A"),
        criado_em=datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime('%d/%m/%Y'),
        seguidores=user.get("followers", 0),
        public_repos=user.get("public_repos", 0),
        commits=total_commits,
        prs_abertas=total_prs_open,
        prs_fechadas=total_prs_closed,
        branches=total_branches,
        estrelas=total_stars,
        forks=total_forks,
        linguagens=linguagens,
        avatar_url=user.get("avatar_url", "")
    )


def baixar_avatar(url, caminho="avatar.png"):
    resp = requests.get(url)
    print(f"Status do avatar: {resp.status_code}")
    if resp.status_code == 200:
        with open(caminho, "wb") as f:
            f.write(resp.content)
        return caminho
    return None


#Estatísticas do REPOSITÓRIO


def get_github_data(owner: str, repo: str, endpoint: str = ""):
    url = f"https://api.github.com/repos/{owner}/{repo}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def info_repositorio(owner: str, repo: str) -> Dict:
    # Dados do repositório
    repo_data = get_github_data(owner, repo)
    stars = repo_data.get("stargazers_count", 0)
    forks = repo_data.get("forks_count", 0)
    watchers = repo_data.get("watchers_count", 0)
    size_kb = repo_data.get("size", 0)
    updated_at = repo_data.get("updated_at", "")

    # Contribuidores
    contributors = get_github_data(owner, repo, "/contributors")
    top_contributors = [
        f"- {contrib['login']} ({contrib.get('contributions', 0)} commits)"
        for contrib in contributors[:10]
    ]

    # Linguagens
    languages = get_github_data(owner, repo, "/languages")
    language_lines = [
        f"- {lang}: {lines} linhas"
        for lang, lines in languages.items()
    ]

    # Resposta formatada
    return {
        "Estrelas": stars,
        "Forks": forks,
        "Watchers": watchers,
        "Tamanho": f"{size_kb} KB",
        "Última atualização": updated_at,
        "Top 10 Contribuidores": top_contributors,
        "Linguagens Utilizadas": language_lines
    }


# Gráfico de commits por repositórios do USUÁRIO


def coletar_commits_por_repositorio(usuario: str):
    repos_url = f"https://api.github.com/users/{usuario}/repos?per_page=100"
    resp = requests.get(repos_url, headers=HEADERS)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.json().get("message"))

    repos = resp.json()
    commits_por_repo = {}

    for repo in repos:
        repo_name = repo["name"]
        owner = repo["owner"]["login"]

        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?per_page=100"
        commits_resp = requests.get(commits_url, headers=HEADERS)

        if commits_resp.status_code == 200:
            commits_por_repo[repo_name] = len(commits_resp.json())
        else:
            print(f"Erro ao coletar commits de {repo_name}: {commits_resp.status_code}")

    return commits_por_repo


# Gráfico de commits por data do REPOSITÓRIO 


def get_commit_count(request: RepoRequest):
    url = f"https://api.github.com/repos/{request.owner}/{request.repo}/commits"
    
    response = requests.get(url)
    
    commits = response.json() 
    
    commits_count = {}


    for commit in commits:
        commit_date = commit["commit"]["author"]["date"][:10]
        commits_count[commit_date] = commits_count.get(commit_date, 0) + 1

    sorted_dates = sorted(commits_count.keys())
    sorted_counts = [commits_count[date] for date in sorted_dates]
        
    return sorted_dates, sorted_counts
