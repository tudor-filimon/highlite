# Upload routes
#
# POST /upload
# - Accept video file as multipart form data
# - Accept optional keywords query param or form field
# - Save file to temp directory
# - Create job in memory store (status=processing)
# - Queue background task: process_video(job_id)
# - Return job_id immediately
#
# Note: File uploaded directly to backend, no external storage
