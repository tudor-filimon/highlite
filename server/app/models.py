# Pydantic models for request/response validation
#
# Enums:
# - JobStatus: pending, uploading, processing, completed, failed
#
# Request Models:
# - UploadInitRequest: filename, keywords (optional)
# - UploadCompleteRequest: job_id
#
# Response Models:
# - UploadInitResponse: job_id, upload_url, video_path
# - UploadCompleteResponse: job_id, status
# - JobStatusResponse: job_id, status, progress, highlight_url, error_message
# - JobDetailResponse: Full job details including metadata
#
# Internal Models:
# - Highlight: start, end, description
