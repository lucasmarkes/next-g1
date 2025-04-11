import os
import requests
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from models_github import RepoStats


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


#Estatísticas do REPOSITÓRIO


def get_github_data(owner: str, repo: str, endpoint: str = ""):
    url = f"https://api.github.com/repos/{owner}/{repo}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def info_repositorio(owner: str, repo: str) -> RepoStats:
    repo_data = get_github_data(owner, repo)
    stars = repo_data.get("stargazers_count", 0)
    forks = repo_data.get("forks_count", 0)
    watchers = repo_data.get("watchers_count", 0)
    size_kb = repo_data.get("size", 0)
    updated_at = repo_data.get("updated_at", "")

    # Funções auxiliares (contribuidores e linguagens) para rodar em paralelo
    def fetch_contributors():
        contributors = get_github_data(owner, repo, "/contributors")
        return [
            f"- {c['login']} ({c.get('contributions', 0)} commits)"
            for c in contributors[:10]
        ]

    def fetch_languages():
        languages = get_github_data(owner, repo, "/languages")
        return [f"- {lang}: {lines} linhas" for lang, lines in languages.items()]

    # Executar em paralelo com concurrent.futures
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_contributors = executor.submit(fetch_contributors)
        future_languages = executor.submit(fetch_languages)

        top_contribuidores = future_contributors.result()
        linguagens_utilizadas = future_languages.result()

    return RepoStats(
        estrelas=stars,
        forks=forks,
        watchers=watchers,
        tamanho=f"{size_kb} KB",
        ultima_atualizacao=updated_at,
        top_contribuidores=top_contribuidores,
        linguagens_repo=linguagens_utilizadas
    )


# Gráfico de commits por data do REPOSITÓRIO


def get_commit_count(owner: str, repo: str):
    commits = get_github_data(owner, repo, "/commits?per_page=100")
    
    commits_count = {}


    for commit in commits:
        commit_date = commit["commit"]["author"]["date"][:10]
        commits_count[commit_date] = commits_count.get(commit_date, 0) + 1

    sorted_dates = sorted(commits_count.keys())
    sorted_counts = [commits_count[date] for date in sorted_dates]
        
    return sorted_dates, sorted_counts
