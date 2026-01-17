# Pydantic models for request/response validation
#
# Enums:
# - JobStatus: pending, processing, completed, failed
#
# Request Models:
# - UploadRequest: keywords (optional) - file sent as multipart form
#
# Response Models:
# - UploadResponse: job_id
# - JobStatusResponse: job_id, status, progress, error_message
#
# Internal Models:
# - Job: id, status, progress, keywords, video_path, highlight_path, error
# - Highlight: start, end, description
#
# Note: No database - jobs stored in memory dict