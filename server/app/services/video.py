# FFmpeg video processing service
#
# Methods:
# - get_video_duration(video_path) -> float seconds (using ffprobe)
# - split_video(input_path, output_dir) -> list[(chunk_path, time_offset)]
#   - Split into 10-15 min chunks with 10 sec overlap
#   - Uses -c copy for fast splitting (no re-encoding)
# - extract_clip(input_path, start, end, output_path) -> clip path
#   - Uses -c copy for fast extraction
# - extract_clips_parallel(input_path, markers, output_dir) -> list[clip_paths]
#   - Extract clips for each detected marker in parallel
#   - Filename format: marker_{index}_{type}_{start}s.mp4
#
# Note: No concatenation needed - we keep individual clips
