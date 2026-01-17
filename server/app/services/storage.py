# Supabase Storage service
#
# Methods:
# - create_upload_url(path) -> presigned URL for frontend direct upload
# - get_public_url(path) -> public URL for TwelveLabs URL ingestion
# - create_signed_url(path, expires_in) -> temporary signed URL
# - download(path) -> bytes
# - upload(path, data) -> public URL
# - delete(path) -> None
# - list_files(prefix) -> list of files
# - cleanup_job_files(job_id) -> delete original + chunks, keep highlight reel
