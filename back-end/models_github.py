from pydantic import BaseModel
from typing import List


class Limite (Exception):
    def __init__(self):
        super().__init__(
            "Atenção: poucas requisições restantes na API do GitHub.\n"
            "Operação interrompida para evitar bloqueio por limite."
        )

class LinguagemStats(BaseModel):
    linguagem: str
    porcentagem: float

class RepoStats(BaseModel):
    estrelas: int
    forks: int
    watchers: int
    tamanho: str
    ultima_atualizacao: str
    contribuidores: List[str]
    linguagens_repo: List[str]

class UserStats(BaseModel):
    seguidores: int
    public_repos: int
    forks: int
    estrelas: int
    commits: int
    branches: int
    prs_total: int
    linguagens: List[LinguagemStats]
    repositorios: List[str]
