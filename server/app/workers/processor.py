# Background video processing pipeline
#
# Main function: process_video(job_id, video_path, keywords)
#
# Pipeline steps:
# 1. Download original video from Supabase (progress: 10%)
# 2. Split into 6-9 chunks of 10-15 min with overlap (progress: 20%)
# 3. Upload chunks to Supabase, get public URLs (progress: 30%)
# 4. PARALLEL: Analyze all chunks via TwelveLabs URL ingestion (progress: 40-70%)
# 5. Merge timestamps + deduplicate overlapping highlights (progress: 70%)
# 6. PARALLEL: Extract all clips with FFmpeg (progress: 75-85%)
# 7. Concatenate clips into final highlight reel (progress: 85%)
# 8. Upload highlight reel to Supabase (progress: 90%)
# 9. Update job status to completed (progress: 100%)
# 10. Cleanup: delete original video + chunks (keep only highlight reel)
#
# Helper functions:
# - update_job_progress(job_id, progress, status)
# - update_job_failed(job_id, error_message)
# - merge_and_dedupe_highlights(chunk_results) -> deduplicated list