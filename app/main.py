from fastapi import FastAPI
from api.analyze_repo import router

app = FastAPI(title="AI Code Understanding Agent")
app.include_router(router)
