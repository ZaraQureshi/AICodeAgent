from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path

from tools.repo_scanner import clone_and_scan
from agent.code_understanding_agent import code_understanding_agent

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/analyze")
def analyze_repo(req: RepoRequest):
    repo_data = clone_and_scan(req.repo_url)
    print(repo_data)
   
    important_files = [
        f for f in repo_data["file_tree"]
        if any(k in f.lower() for k in ["main", "app", "index", "server"])
    ][:6]

    code_chunks = []
    for file in important_files:
        path = repo_data["repo_path"] / file
        try:
            code_chunks.append(path.read_text(errors="ignore")[:3000])
        except Exception:
            continue
    summary = code_understanding_agent(
        repo_data["file_tree"][:40],
        code_chunks
    )

    return {
    "understanding": summary
    }

