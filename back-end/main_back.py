from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from github_utils import buscar_estatisticas
from models_github import GithubStats, RepoRequest
from repo_graph_commits import repo_graph_commits_date
from user_graph_commits import user_graph_commits_repos
from pdf_repo_gerar import gerar_pdf_repo
from pdf_user_gerar import gerar_pdf_usuario


load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"}


app = FastAPI()


@app.get("/github/{usuario}", response_model=GithubStats)
def obter_estatisticas(usuario: str):
    return buscar_estatisticas(usuario)


@app.get("/relatorio/{usuario}")
def pdf_user(usuario: str):
    caminho_pdf = gerar_pdf_usuario(usuario)
    return FileResponse(caminho_pdf, media_type="application/pdf", filename=caminho_pdf)


@app.get("/grafico/{usuario}")
def user_graph_commits(usuario: str):
    return user_graph_commits_repos(usuario)


@app.get("/repo/info")
def info_repositorio(owner: str, repo: str):
    request = RepoRequest(owner=owner, repo=repo)
    repo_data = get_github_data(request, "")
    contributors = get_github_data(request, "/contributors")
    languages = get_github_data(request, "/languages")

    return {
        "repo": repo_data,
        "contributors": contributors[:5],
        "languages": languages
    }


@app.get("/relatorio/{owner}/{repo}")
def pdf_repo(owner: str, repo: str):
    caminho_pdf = gerar_pdf_repo(owner, repo)
    return FileResponse(caminho_pdf, media_type='application/pdf', filename=caminho_pdf)


@app.post("/grafico/repo")
def repo_graph_commits(request: RepoRequest):
    return repo_graph_commits_date(request)