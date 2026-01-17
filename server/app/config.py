from pydantic_settings import BaseSettings
from functools import lru_cache
import tempfile
import os


class Settings(BaseSettings):
    # TwelveLabs
    twelvelabs_api_key: str = ""
    
    # Default autism markers to detect
    default_markers: str = (
        "hand_flapping,rocking,spinning,toe_walking,"
        "limited_eye_contact,lack_of_social_engagement,"
        "echolalia,limited_verbal_response,"
        "covering_ears,unusual_sensory_response,"
        "object_lining,repetitive_play"
    )
    
    # Video processing
    chunk_duration_seconds: int = 900  # 15 minutes
    chunk_overlap_seconds: int = 10
    
    # CORS
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # Temp directory for video processing
    temp_dir: str = os.path.join(tempfile.gettempdir(), "highlite")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
