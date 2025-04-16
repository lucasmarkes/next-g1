import os
import requests
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from models_github import RepoStats, Limite


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


#Estatísticas do REPOSITÓRIO


def get_github_data(owner: str, repo: str, endpoint: str = ""):
    url = f"https://api.github.com/repos/{owner}/{repo}{endpoint}"
    
    try:
        # Definindo o tempo limite para 10 segundos
        resp = requests.get(url, headers=HEADERS, timeout=10)

         # Verifica o limite de requisições restante
        remaining = int(resp.headers.get("X-RateLimit-Remaining", 1000))
        
        # Se o limite estiver prestes a ser atingido, interrompe e informa o usuário
        if remaining < 5:
            raise Limite
        
        # Se a requisição for bem-sucedida, retorna os dados no formato JSON
        return resp.json()
    
    except Limite as e:
        print(f"Erro de limite de requisições: {e}")
        return {"operação impedida": str(e)}
    

    except requests.exceptions.Timeout:
        print("A requisição excedeu o tempo de espera.")

    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro na requisição: {e}')

    return None


def info_repositorio(owner: str, repo: str) -> RepoStats:  
    repo_data = get_github_data(owner, repo)

    if not repo_data:
        return RepoStats(
            estrelas=0,
            forks=0,
            watchers=0,
            tamanho="N/A",
            ultima_atualizacao="N/A",
            contribuidores=["Erro ao acessar dados / repositório muito grande."],
            linguagens_repo=["Erro ao acessar dados / repositório muito grande."]
        )

    stars = repo_data.get("stargazers_count", 0)
    forks = repo_data.get("forks_count", 0)
    watchers = repo_data.get("watchers_count", 0)
    size_kb = repo_data.get("size", 0)
    updated_at = repo_data.get("updated_at", "N/A")
    

    # Funções auxiliares (contribuidores e linguagens) para rodar em paralelo
    def fetch_contributors():
        contributors = get_github_data(owner, repo, "/contributors")
        if isinstance(contributors, list):
            return [f"- {c['login']} ({c.get('contributions', 0)} commits)" for c in contributors[:10]]
        return ["Não foi possível obter contribuidores (repositório muito grande)."]

    def fetch_languages():
        languages = get_github_data(owner, repo, "/languages")
        if isinstance(languages, dict):
            sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]
            return [f"- {lang}: {bytes} bytes" for lang, bytes in sorted_languages]
        return ["Não foi possível obter linguagens (repositório muito grande)."]

    # Executar em paralelo com concurrent.futures
    try: 
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_contributors = executor.submit(fetch_contributors)
            future_languages = executor.submit(fetch_languages)            

            contribuidores_result = future_contributors.result()
            linguagens_utilizadas = future_languages.result()

            if any(isinstance(r, dict) and "operação impedida" in r for r in [contribuidores_result, linguagens_utilizadas]):
                print("Erro ao executar em paralelo: limite de requisições atingido.")
                contribuidores_result = ["Erro ao processar os dados."]
                linguagens_utilizadas = ["Erro ao processar os dados."]

    except Exception as e:
        print(f"Erro inesperado: {e}")
        contribuidores_result = ["Erro ao processar os dados (repositório muito grande ou limite da API)."]
        linguagens_utilizadas = ["Erro ao processar os dados (repositório muito grande ou limite da API)."]


    return RepoStats(
        estrelas=stars,
        forks=forks,
        watchers=watchers,
        tamanho=f"{size_kb} KB",
        ultima_atualizacao=updated_at,
        contribuidores = contribuidores_result,
        linguagens_repo=linguagens_utilizadas
    )


# Gráfico de commits por data do REPOSITÓRIO


def get_commit_count(owner: str, repo: str, intervalo: int = 30):
    commits = get_github_data(owner, repo, "/commits?per_page=100")
    
    if not commits or not isinstance(commits, list):
        print(f"Erro ao buscar commits para {owner}/{repo}.")
        return [], []
    
    commits_count = {}

    for commit in commits:
        try:
            commit_date = commit["commit"]["author"]["date"][:10]
            commits_count[commit_date] = commits_count.get(commit_date, 0) + 1
        except KeyError as e:
            print(f"Erro ao buscar commits para {owner}/{repo} : {e}")
            return None

    sorted_dates = sorted(commits_count.keys())

    if intervalo:
        sorted_dates = sorted_dates[-intervalo:]
        
    sorted_counts = [commits_count[date] for date in sorted_dates]
        
    return sorted_dates, sorted_counts
