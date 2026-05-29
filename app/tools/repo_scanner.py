from git import Repo
from pathlib import Path
import tempfile

BASE_PATH = Path(tempfile.gettempdir()) / "code_repos"

def clone_and_scan(repo_url: str) -> dict:
    BASE_PATH.mkdir(exist_ok=True)

    repo_path = BASE_PATH / str(abs(hash(repo_url)))

    if not repo_path.exists():
        Repo.clone_from(repo_url, repo_path)

    files = [
        str(p.relative_to(repo_path))
        for p in repo_path.rglob("*")
        if p.is_file() and p.suffix in {".py", ".js", ".ts", ".java", ".go"}
    ]
    print("here",repo_path,files)
    return {
        "repo_path": repo_path,
        "file_tree": files
    }
