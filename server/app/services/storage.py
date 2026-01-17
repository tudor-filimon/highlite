import os
import uuid
import shutil
import json
from pathlib import Path
from typing import Optional
from app.config import get_settings
from app.models import Job, JobStatus

settings = get_settings()

# In-memory job store
_jobs: dict[str, Job] = {}


def create_job(markers: list[str]) -> Job:
    """Create a new job and its temp directory."""
    job_id = str(uuid.uuid4())
    job_dir = get_job_dir(job_id)
    
    # Create directories
    os.makedirs(job_dir, exist_ok=True)
    os.makedirs(os.path.join(job_dir, "chunks"), exist_ok=True)
    os.makedirs(os.path.join(job_dir, "clips"), exist_ok=True)
    
    job = Job(
        id=job_id,
        status=JobStatus.PENDING,
        markers=markers,
    )
    _jobs[job_id] = job
    return job


def get_job(job_id: str) -> Optional[Job]:
    """Get job by ID."""
    return _jobs.get(job_id)


def update_job(job_id: str, **updates) -> Optional[Job]:
    """Update job fields."""
    job = _jobs.get(job_id)
    if job:
        for key, value in updates.items():
            if hasattr(job, key):
                setattr(job, key, value)
    return job


def get_job_dir(job_id: str) -> str:
    """Get the temp directory path for a job."""
    return os.path.join(settings.temp_dir, job_id)


def get_video_path(job_id: str) -> str:
    """Get path for original video."""
    return os.path.join(get_job_dir(job_id), "original.mp4")


def get_chunks_dir(job_id: str) -> str:
    """Get path for chunks directory."""
    return os.path.join(get_job_dir(job_id), "chunks")


def get_clips_dir(job_id: str) -> str:
    """Get path for clips directory."""
    return os.path.join(get_job_dir(job_id), "clips")


def get_report_path(job_id: str) -> str:
    """Get path for report JSON file."""
    return os.path.join(get_job_dir(job_id), "report.json")


def save_report(job_id: str, report: dict) -> str:
    """Save report to JSON file."""
    report_path = get_report_path(job_id)
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    return report_path


def load_report(job_id: str) -> Optional[dict]:
    """Load report from JSON file."""
    report_path = get_report_path(job_id)
    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            return json.load(f)
    return None


def list_clips(job_id: str) -> list[str]:
    """List all clip files for a job."""
    clips_dir = get_clips_dir(job_id)
    if not os.path.exists(clips_dir):
        return []
    return sorted([f for f in os.listdir(clips_dir) if f.endswith(".mp4")])


def get_clip_path(job_id: str, filename: str) -> Optional[str]:
    """Get full path for a specific clip."""
    clip_path = os.path.join(get_clips_dir(job_id), filename)
    if os.path.exists(clip_path):
        return clip_path
    return None


def cleanup_job(job_id: str, keep_results: bool = True) -> None:
    """Clean up temp files for a job."""
    job_dir = get_job_dir(job_id)
    
    if keep_results:
        # Delete original video and chunks, keep clips and report
        for item in ["original.mp4", "chunks"]:
            path = os.path.join(job_dir, item)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    else:
        # Delete entire job directory
        if os.path.exists(job_dir):
            shutil.rmtree(job_dir)
        # Remove from memory
        _jobs.pop(job_id, None)
