# TwelveLabs API service
#
# Methods:
# - ensure_index(index_name) -> create or get existing index
# - analyze_video_from_url(video_url, keywords, time_offset) -> list[Highlight]
#   - Uses URL ingestion (TwelveLabs fetches from Supabase URL)
#   - Calls summarize(type="highlight") with keyword-based prompt
#   - Applies time_offset to returned timestamps
# - _build_prompt(keywords) -> prompt string for TwelveLabs
