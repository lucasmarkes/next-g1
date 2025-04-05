from pydantic import BaseModel
import requests
from typing import Dict, List

class RepoRequest(BaseModel):
    owner: str
    repo: str

class LinguagemStats(BaseModel):
    linguagem: str
    porcentagem: float

class GithubStats(BaseModel):
    nome: str
    login: str
    localizacao: str
    criado_em: str
    seguidores: int
    public_repos: int
    commits: int
    prs_abertas: int
    prs_fechadas: int
    branches: int
    estrelas: int
    forks: int
    linguagens: List[LinguagemStats]
    avatar_url: str
