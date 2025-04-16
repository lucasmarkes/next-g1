import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from datetime import datetime
from models_github import LinguagemStats, UserStats, Limite


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


#Estatísticas do USUÁRIO - módulos separados


# Centralizar tratamento de erros
def get_github(url: str, timeout: int = 10, headers: dict = HEADERS) -> dict | list | None:
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)

        # Verifica o limite de requisições restante
        remaining = int(resp.headers.get("X-RateLimit-Remaining", 1000))
        
        # Se o limite estiver prestes a ser atingido, interrompe e informa o usuário
        if remaining < 5:
            raise Limite (f"Não podemos completar a análise desses dados: o limite de requisições permitidas pelo GitHub seria atingido.")
        
        return resp.json()
    
    except Limite as e:
        print(f"Erro de limite de requisições: {e}")
        return {"operação impedida": str(e)}

    except requests.exceptions.Timeout:
        print(f"Timeout na URL: {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição: {url} — {e}")

    return None


# Dados básicos do usuário
def buscar_usuario(usuario: str) -> dict:
    url = f"https://api.github.com/users/{usuario}"
    user = get_github(url)
    if user:
        return {
            "nome": user.get("name", "N/A"),
            "login": user.get("login", "N/A"),
            "localizacao": user.get("location", "N/A"),
            "criado_em": datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime('%d/%m/%Y'),
            "avatar_url": user.get("avatar_url", "")
        }
    return {"erro": f"Usuário {usuario} não encontrado"}


# Baixar o avatar (imagem)
def baixar_avatar(url, caminho="avatar.png"):
    resp = get_github(url)
    if resp.status_code == 200:
        with open(caminho, "wb") as f:
            f.write(resp.content)
        return caminho
    return None


# Permite que as outras funções verifiquem os dados totais (em todos os repositórios disponíveis)
def buscar_repositorios(usuario: str) -> list:
    url = f"https://api.github.com/users/{usuario}/repos?per_page=100"
    repos = []
    page = 1

    while True:
        resp = requests.get(f"{url}&page={page}", headers=HEADERS)
        if resp.status_code != 200:
            break

        dados = resp.json()
        if not dados:
            break

        repos.extend(dados)
        page += 1

    return repos


# Seguidores e Número de repositórios 
def buscar_dados_gerais(usuario: str) -> dict:
    url = f"https://api.github.com/users/{usuario}"
    user = get_github(url)
    if user:
        return {
            "seguidores": user.get("followers", 0),
            "public_repos": user.get("public_repos", 0),
        }

# Todas as estatisticas usadas no front-end
def buscar_estatisticas(usuario: str) -> UserStats:
    try:
        repos = buscar_repositorios(usuario)

        def contar_commits(repo):
            url = f"https://api.github.com/repos/{usuario}/{repo['name']}/commits?per_page=100"
            resp = get_github(url)
            return len(resp.json()) if resp.status_code == 200 else 0

        def contar_branches(repo):
            url = f"https://api.github.com/repos/{usuario}/{repo['name']}/branches?per_page=100"
            resp = get_github(url)
            return len(resp.json()) if resp.status_code == 200 else 0

        def contar_total_prs(repo):
            total = 0
            for state in ["open", "closed"]:
                url = f"https://api.github.com/repos/{usuario}/{repo['name']}/pulls?state={state}&per_page=100"
                resp = get_github(url)
                if resp.status_code == 200:
                    total += len(resp.json())
            return total

        def obter_linguagens(repo):
            url = f"https://api.github.com/repos/{usuario}/{repo['name']}/languages"
            resp = get_github(url)
            return resp.json() if resp.status_code == 200 else {}

        with ThreadPoolExecutor(max_workers=10) as executor:
            commits_futures = executor.map(contar_commits, repos)
            branches_futures = executor.map(contar_branches, repos)
            prs_futures = executor.map(contar_total_prs, repos)
            linguagens_futures = executor.map(obter_linguagens, repos)

        total_commits = sum(commits_futures)
        total_branches = sum(branches_futures)
        total_prs = sum(prs_futures)

        linguagens_totais = {}
        for lang_dict in linguagens_futures:
            for lang, qtd in lang_dict.items():
                linguagens_totais[lang] = linguagens_totais.get(lang, 0) + qtd

        total_linhas = sum(linguagens_totais.values())
        linguagens_ordenadas = sorted(linguagens_totais.items(), key=lambda x: x[1], reverse=True)

        linguagens = [
            {"linguagem": lang, "porcentagem": (qtd / total_linhas) * 100}
            for lang, qtd in linguagens_ordenadas[:10]
        ] if total_linhas > 0 else []

        forks = sum(repo.get("forks_count", 0) for repo in repos)
        estrelas = sum(repo.get("stargazers_count", 0) for repo in repos)
        dados_gerais = buscar_dados_gerais(usuario)

        return UserStats(
            seguidores=dados_gerais["seguidores"],
            public_repos=dados_gerais["public_repos"],
            forks=forks,
            estrelas=estrelas,
            commits=total_commits,
            branches=total_branches,
            prs_total=total_prs,
            linguagens=[LinguagemStats(**l) for l in linguagens],
            repositorios = [repo["name"] for repo in repos if not repo.get("private", False)]
        )
    
    except Limite as e:
        print(f"operação impedida: {e}")
        raise Limite (f"Não podemos completar a análise desses dados: o limite de requisições permitidas pelo GitHub seria atingido.")

    except requests.exceptions.Timeout:
        print(f"Timeout na URL: {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição: {url} — {e}")


# Gráfico de commits por repositórios do USUÁRIO


def coletar_commits_por_repositorio(usuario: str):
    repos = buscar_repositorios(usuario) 
    commits_por_repo = {}

    def fetch_commits(repo):
        repo_name = repo["name"]
        owner = repo["owner"]["login"]
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?per_page=100"
        commits_resp = get_github(commits_url)

        if commits_resp is None:
            return repo_name, 0  # Retorna o nome do repositório e 0 commits caso a requisição falhe
        return repo_name, len(commits_resp)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_commits, repo) for repo in repos]
        for future in as_completed(futures):
            repo_name, commits_count = future.result()
            commits_por_repo[repo_name] = commits_count

    return commits_por_repo
