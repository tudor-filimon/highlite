# Upload routes
#
# POST /upload/init
# - Generate presigned URL for direct Supabase upload
# - Create job record in database (status=uploading)
# - Return job_id and upload_url
#
# POST /upload/complete
# - Called after frontend completes direct upload
# - Update job status to processing
# - Queue background task: process_video(job_id, video_path, keywords)
# - Return job_id and status
