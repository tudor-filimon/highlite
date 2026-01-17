# TwelveLabs API service
#
# Methods:
# - ensure_index(index_name) -> create or get existing index
# - analyze_video_from_file(video_path, keywords, time_offset) -> list[Highlight]
#   - Uses DIRECT FILE UPLOAD (not URL ingestion)
#   - Calls summarize(type="highlight") with keyword-based prompt
#   - Applies time_offset to returned timestamps
# - _build_prompt(keywords) -> prompt string for TwelveLabs
#
# Note: Direct file upload instead of URL ingestion
# This works on localhost and doesn't require external storage