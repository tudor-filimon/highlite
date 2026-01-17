from datetime import datetime
from app.services import storage
from app.models import JobStatus


async def process_video(job_id: str):
    """
    Background video processing pipeline for autism marker detection.
    
    Steps:
    1. Get video info and duration
    2. Split into chunks if needed
    3. Upload to TwelveLabs and analyze for markers (parallel)
    4. Merge marker results from all chunks
    5. Extract individual clips for each marker (parallel)
    6. Generate report.json
    7. Cleanup temp files
    """
    try:
        storage.update_job(job_id, status=JobStatus.PROCESSING, progress=5)
        
        job = storage.get_job(job_id)
        if not job:
            return
        
        # TODO: Implement processing steps
        
        # Step 1: Get video duration (progress: 10%)
        storage.update_job(job_id, progress=10)
        video_duration = 0.0  # TODO: Get actual duration with ffprobe
        
        # Step 2: Split into chunks if needed (progress: 15%)
        storage.update_job(job_id, progress=15)
        # TODO: Split video into chunks
        
        # Step 3-4: TwelveLabs analysis (progress: 20-70%)
        storage.update_job(job_id, progress=20)
        # TODO: Upload to TwelveLabs and analyze
        markers = []  # Will be populated by TwelveLabs
        
        # Step 5: Extract clips (progress: 75-90%)
        storage.update_job(job_id, progress=75)
        # TODO: Extract clips using FFmpeg
        
        # Step 6: Generate report (progress: 95%)
        storage.update_job(job_id, progress=95)
        
        # Create marker counts
        marker_counts = {}
        for marker in markers:
            marker_type = marker.get("type", "unknown")
            marker_counts[marker_type] = marker_counts.get(marker_type, 0) + 1
        
        report = {
            "job_id": job_id,
            "video_duration": video_duration,
            "analysis_date": datetime.now().isoformat(),
            "markers": markers,
            "summary": "Analysis complete. See individual markers for details.",
            "marker_counts": marker_counts,
            "total_markers": len(markers)
        }
        
        report_path = storage.save_report(job_id, report)
        
        # Step 7: Mark complete
        storage.update_job(
            job_id,
            status=JobStatus.COMPLETED,
            progress=100,
            report_path=report_path
        )
        
        # Cleanup temp files (keep clips and report)
        storage.cleanup_job(job_id, keep_results=True)
        
    except Exception as e:
        storage.update_job(
            job_id,
            status=JobStatus.FAILED,
            error_message=str(e)
        )
