from repo_requests import get_commit_count
import matplotlib.pyplot as plt
import io
from fastapi.responses import Response

def repo_graph_commits_date(owner: str, repo: str):
    sorted_dates, sorted_counts = get_commit_count(owner, repo)
    
    plt.figure(figsize=(10,5))
    plt.plot(sorted_dates,sorted_counts,marker="o",linestyle="-",color="b")
    plt.xlabel("data")
    plt.ylabel("commit")
    plt.title(f"Commits por data-{owner}/{repo}")
    plt.xticks(rotation=45)
    plt.grid(True)
    
    
    buffer = io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    plt.close()

    return Response(content=buffer.getvalue(),media_type="image/png") 