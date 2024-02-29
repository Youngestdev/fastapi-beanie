from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from server.database import init_db
from server.routes.product_review import router as Router


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    """Initialize database"""
    await init_db()
    print("Startup complete")
    yield
    print("Shutdown complete")


app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/swagger",
    redoc_url=None,
    title="FastAPI-beanie",
    description="FastAPI services demo",
    version="0.2.0",
    lifespan=lifespan,
    servers=[
        {"url": "http://localhost:8000", "description": "Local environment"},
    ],
)
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
