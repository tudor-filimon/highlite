# Jobs routes
#
# GET /jobs/{job_id}/status
# - Return job status and progress from in-memory store
# - Frontend polls this every 3 seconds
#
# GET /jobs/{job_id}/download
# - Return highlight reel as file download (StreamingResponse)
# - Only available when status=completed
# - After download, optionally cleanup temp files
#
# Note: Jobs stored in memory dict, files in temp directory
