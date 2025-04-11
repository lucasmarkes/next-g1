from fastapi import HTTPException
import matplotlib.pyplot as plt
from user_requests import coletar_commits_por_repositorio
from io import BytesIO
from fastapi.responses import StreamingResponse

def user_graph_commits_repos(usuario: str):
    commits_por_repo = coletar_commits_por_repositorio(usuario)

    if not commits_por_repo:
        raise HTTPException(status_code=404, detail="Nenhum dado de commits encontrado.")

    nomes = list(commits_por_repo.keys())[:10]
    valores = list(commits_por_repo.values())[:10]

    plt.figure(figsize=(10, 5))
    plt.bar(nomes, valores, color="skyblue")
    plt.xticks(rotation=45, ha='right')
    plt.title("Commits por Repositório")
    plt.ylabel("Quantidade de Commits")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return StreamingResponse(buf, media_type="image/png")
