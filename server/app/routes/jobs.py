# Jobs routes
#
# GET /jobs/{job_id}/status
# - Return job status, progress (0-100), highlight_url (if complete)
# - Frontend polls this every 3 seconds
#
# GET /jobs/{job_id}
# - Return full job details including highlights_metadata
