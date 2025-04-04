from fastapi import FastAPI
import requests
from pydantic import BaseModel
import matplotlib.pyplot as plt
import io
from fastapi.responses import Response

app = FastAPI()

class RepoRequest(BaseModel):
    owner: str
    repo: str

@app.post("/repos")
def get_commit_count(request: RepoRequest):
    url = f"https://api.github.com/repos/{request.owner}/{request.repo}/commits"
    
    response = requests.get(url)
    
    commits = response.json() 
    
    commits_count = {}


    for commit in commits:
        commit_date = commit["commit"]["author"]["date"][:10]
        commits_count[commit_date] = commits_count.get(commit_date, 0) + 1
    

    sorted_dates = sorted(commits_count.keys())
    sorted_counts = [commits_count[date] for date in sorted_dates]


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