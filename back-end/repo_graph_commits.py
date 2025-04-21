from repo_requests import get_commit_count
import matplotlib.pyplot as plt
import io
from fastapi.responses import Response

def repo_graph_commits_date(owner: str, repo: str, intervalo: int = 30):
    sorted_dates, sorted_counts = get_commit_count(owner, repo, intervalo)
    
    plt.figure(figsize=(11,6))
    plt.plot(sorted_dates,sorted_counts,marker="o",linestyle="-",color="b")
    plt.xlabel("Datas")
    plt.ylabel("Commits")
    # plt.title(f"Commits por data-{owner}/{repo}") | Grupo optou pelo título na page do Front-end
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    
    
    buffer = io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    plt.close()

    return Response(content=buffer.getvalue(),media_type="image/png") 