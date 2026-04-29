from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router as api_router


app = FastAPI(
    title="AI-Powered Document Review & Risk Insights Platform",
    description=(
        "Analyze business documents to generate summaries, key entities, risk flags, "
        "and recommended action items."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501",
        "http://127.0.0.1:8000",
        "http://localhost:5500",
        "http://localhost:5501",
        "http://localhost:8000",
        "file://",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "AI-Powered Document Review & Risk Insights Platform is running.",
        "docs": "/docs",
    }
