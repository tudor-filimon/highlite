import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models import (
    JobStatusResponse, 
    JobStatus, 
    ReportResponse, 
    MarkerResponse,
    ClipsListResponse,
    ClipInfo
)
from app.services import storage

router = APIRouter()


@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """
    Get the current status and progress of a job.
    Frontend should poll this every 3 seconds.
    """
    job = storage.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobStatusResponse(
        job_id=job.id,
        status=job.status,
        progress=job.progress,
        error_message=job.error_message
    )


@router.get("/{job_id}/report", response_model=ReportResponse)
async def get_report(job_id: str):
    """
    Get the analysis report with all detected markers.
    Only available when job status is 'completed'.
    """
    job = storage.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job is not complete. Current status: {job.status}"
        )
    
    report = storage.load_report(job_id)
    
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return ReportResponse(
        job_id=report["job_id"],
        video_duration=report["video_duration"],
        analysis_date=report["analysis_date"],
        markers=[MarkerResponse(**m) for m in report["markers"]],
        summary=report["summary"],
        marker_counts=report["marker_counts"],
        total_markers=report["total_markers"]
    )


@router.get("/{job_id}/clips", response_model=ClipsListResponse)
async def list_clips(job_id: str):
    """
    List all detected marker clips.
    Only available when job status is 'completed'.
    """
    job = storage.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job is not complete. Current status: {job.status}"
        )
    
    report = storage.load_report(job_id)
    clip_files = storage.list_clips(job_id)
    
    clips = []
    for i, filename in enumerate(clip_files):
        # Parse marker info from filename: marker_000_hand_flapping_3.2s.mp4
        marker_info = report["markers"][i] if report and i < len(report["markers"]) else {}
        clips.append(ClipInfo(
            index=i,
            marker_type=marker_info.get("type", "unknown"),
            start=marker_info.get("start", 0),
            end=marker_info.get("end", 0),
            filename=filename
        ))
    
    return ClipsListResponse(
        job_id=job_id,
        total_clips=len(clips),
        clips=clips
    )


@router.get("/{job_id}/clips/{index}")
async def download_clip(job_id: str, index: int):
    """
    Download a specific marker clip by index.
    """
    job = storage.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job is not complete. Current status: {job.status}"
        )
    
    clip_files = storage.list_clips(job_id)
    
    if index < 0 or index >= len(clip_files):
        raise HTTPException(status_code=404, detail="Clip not found")
    
    filename = clip_files[index]
    clip_path = storage.get_clip_path(job_id, filename)
    
    if not clip_path:
        raise HTTPException(status_code=404, detail="Clip file not found")
    
    return FileResponse(
        path=clip_path,
        media_type="video/mp4",
        filename=filename
    )
