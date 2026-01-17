# Background video processing pipeline
#
# Main function: process_video(job_id)
#
# Pipeline steps:
# 1. Get job from memory store, get video path (progress: 5%)
# 2. Split into 6-9 chunks of 10-15 min with overlap (progress: 15%)
# 3. PARALLEL: Upload chunks directly to TwelveLabs + analyze (progress: 20-65%)
#    - Uses direct file upload, not URL ingestion
# 4. Merge timestamps and deduplicate overlapping highlights (progress: 70%)
# 5. PARALLEL: Extract all clips with FFmpeg (progress: 75-85%)
# 6. Concatenate clips into final highlight reel (progress: 90%)
# 7. Update job with highlight_path, status=completed (progress: 100%)
#
# Cleanup: Original video and chunks can be deleted after processing
# Keep highlight_reel.mp4 until user downloads
#
# Helper functions:
# - update_progress(job_id, progress)
# - mark_failed(job_id, error_message)
# - merge_and_dedupe_highlights(chunk_results) -> deduplicated list
#
# Note: All files in local temp directory, jobs in memory
