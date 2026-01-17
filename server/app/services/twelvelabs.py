# TwelveLabs API service for autism marker detection
#
# Methods:
# - ensure_index(index_name) -> create or get existing index
# - analyze_video_for_markers(video_path, markers, time_offset) -> list[Marker]
#   - Uses DIRECT FILE UPLOAD (not URL ingestion)
#   - Custom prompt for autism marker detection
#   - Applies time_offset to returned timestamps
# - _build_autism_prompt(markers) -> prompt string
#
# Autism Detection Prompt Template:
# "Analyze this video of a child for autism behavioral markers.
#  Look for: {markers}
#  For each marker found, provide: type, start time, end time, confidence, description"
