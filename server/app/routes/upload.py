import aiofiles
from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks, HTTPException
from typing import Optional
from app.models import UploadResponse, JobStatus
from app.services import storage
from app.config import get_settings
from app.workers.processor import process_video

router = APIRouter()
settings = get_settings()


@router.post("", response_model=UploadResponse)
async def upload_video(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    markers: Optional[str] = Form(None),
):
    """
    Upload a video file for autism marker analysis.
    
    - file: Video file (MP4, MOV, etc.)
    - markers: Comma-separated markers to look for (optional, uses defaults if empty)
    
    Default markers: hand_flapping, rocking, spinning, toe_walking,
    limited_eye_contact, lack_of_social_engagement, echolalia,
    limited_verbal_response, covering_ears, unusual_sensory_response,
    object_lining, repetitive_play
    """
    # Validate file type
    if not file.content_type or not file.content_type.startswith("video/"):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Please upload a video file."
        )
    
    # Parse markers
    marker_list = []
    if markers:
        marker_list = [m.strip() for m in markers.split(",") if m.strip()]
    if not marker_list:
        marker_list = [m.strip() for m in settings.default_markers.split(",")]
    
    # Create job
    job = storage.create_job(marker_list)
    
    # Save uploaded file to temp directory
    video_path = storage.get_video_path(job.id)
    async with aiofiles.open(video_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):  # 1MB chunks
            await f.write(chunk)
    
    # Update job with video path
    storage.update_job(job.id, video_path=video_path, status=JobStatus.PROCESSING)
    
    # Queue background processing
    background_tasks.add_task(process_video, job.id)
    
    return UploadResponse(
        job_id=job.id,
        status=JobStatus.PROCESSING,
        message="Video uploaded successfully. Analysis started."
    )
