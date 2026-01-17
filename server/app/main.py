from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routes import upload, jobs

settings = get_settings()

app = FastAPI(
    title="Highlite API",
    description="Soccer highlight reel generator using TwelveLabs",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def start_info():
    return {"status": "up and running"}
