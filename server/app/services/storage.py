# Local temp file storage service
#
# In-memory job store: dict[job_id, Job]
#
# Methods:
# - create_job(keywords) -> job_id, creates job dir in temp
# - get_job(job_id) -> Job or None
# - update_job(job_id, **updates) -> None
# - get_job_dir(job_id) -> Path to job's temp directory
# - cleanup_job(job_id) -> Delete all temp files for job
#
# File structure:
# /tmp/highlite/{job_id}/
#   ├── original.mp4      # Uploaded video
#   ├── chunks/           # Split chunks
#   ├── clips/            # Extracted clips  
#   └── highlight_reel.mp4  # Final output
#
# Note: All in-memory, lost on server restart (fine for hackathon)
