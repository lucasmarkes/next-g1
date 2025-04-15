from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pdf_user_gerar import gerar_pdf_user
from user_requests import buscar_estatisticas, buscar_usuario
from repo_requests import info_repositorio
from models_github import UserStats, RepoStats
from repo_graph_commits import repo_graph_commits_date
from user_graph_commits import user_graph_commits_repos
from pdf_repo_gerar import gerar_pdf_repo
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#USUÁRIO


@app.get("/usuario/{usuario}/info")
def info_usuario(usuario: str):
    return buscar_usuario(usuario)


@app.get("/github/{usuario}", response_model=UserStats)
def obter_estatisticas(usuario: str):
    return buscar_estatisticas(usuario)


@app.get("/relatorio/{usuario}")
def pdf_user(usuario: str):
    caminho_pdf = gerar_pdf_user(usuario,nome_arquivo="")
    return FileResponse(caminho_pdf, media_type="application/pdf", filename=caminho_pdf)


@app.get("/grafico/{usuario}")
def user_graph_commits(usuario: str):
    return user_graph_commits_repos(usuario)


#REPOSITÓRIO


@app.get("/github/{owner}/{repo}", response_model=RepoStats)
def estatisticas_repositorio(owner: str, repo: str):
    return info_repositorio(owner, repo)


@app.get("/relatorio/{owner}/{repo}")
def pdf_repo(owner: str, repo: str):
    caminho_pdf = gerar_pdf_repo(owner, repo)
    return FileResponse(caminho_pdf, media_type='application/pdf', filename=caminho_pdf)


@app.get("/grafico/{owner}/{repo}")
def repo_graph_commits(owner: str, repo: str):
    return repo_graph_commits_date(owner, repo)
