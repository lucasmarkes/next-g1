from models_github import RepoRequest
import requests
from github_utils import get_commit_count
import matplotlib.pyplot as plt
import io
from fastapi.responses import Response

def repo_graph_commits_date(request: RepoRequest):
    sorted_dates, sorted_counts = get_commit_count(request)
    
    plt.figure(figsize=(10,5))
    plt.plot(sorted_dates,sorted_counts,marker="o",linestyle="-",color="b")
    plt.xlabel("data")
    plt.ylabel("commit")
    plt.title(f"Commits por data-{request.owner}/{request.repo}")
    plt.xticks(rotation=45)
    plt.grid(True)
    
    
    buffer = io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    plt.close()

    return Response(content=buffer.getvalue(),media_type="image/png") 