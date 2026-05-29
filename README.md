# AICodeAgent

AICodeAgent is a lightweight API that clones a Git repository, scans its structure, extracts key files, and generates a high-level project summary using an LLM-backed code understanding agent.

## Features
- Clone and scan Git repositories
- Identify important entry-point files
- Summarize codebase with an LLM agent
- Simple FastAPI endpoint for analysis

## Tech Stack
- **Backend**: Python, FastAPI, Pydantic  
- **LLM Integration**: OpenAI client wrapper  
- **Utilities**: Git repo cloning and file tree scanning  

## Project Structure
```
app/
  main.py
  agent/
    code_understanding_agent.py
  api/
    analyze_repo.py
  llm/
    openai_client.py
  tools/
    repo_scanner.py
```

## Setup (Windows)

### 1) Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependencies
```
pip install -r requirements.txt
```

### 3) Configure environment variables
Create a `.env` file in the project root and add your OpenAI credentials:
```
OPENAI_API_KEY=your_api_key_here
```

### 4) Run the API
```
uvicorn app.main:app --reload
```

The API will be available at:  
`http://127.0.0.1:8000`

## API Usage

### POST `/analyze`
**Body:**
```json
{
  "repo_url": "https://github.com/owner/repo.git"
}
```

**Response:**
```json
{
  "understanding": "High-level summary of the repository..."
}
```

## Notes
- Ensure Git is installed and available in your PATH.
- The service reads and truncates file content to keep prompts concise.
- If you add new modules, keep them under `app/` for consistency.