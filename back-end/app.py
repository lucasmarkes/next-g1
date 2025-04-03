from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class RepoRequest(BaseModel):
    owner: str
    repo: str

@app.post("/repos")
def get_commit_count(request: RepoRequest):
    url = f"https://api.github.com/repos/{request.owner}/{request.repo}/commits"
    
    response = requests.get(url)
    
    commits = response.json() 
    
    return {"repository": f"{request.owner}/{request.repo}", "commit_count": len(commits)}