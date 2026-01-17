# FFmpeg video processing service
#
# Methods:
# - get_video_duration(video_path) -> float seconds (using ffprobe)
# - split_video(input_path, output_dir) -> list[(chunk_path, time_offset)]
#   - Split into 10-15 min chunks with 10 sec overlap
#   - Uses -c copy for fast splitting (no re-encoding)
# - extract_clip(input_path, start, end, output_path) -> clip path
#   - Uses -c copy for fast extraction
# - concatenate_clips(clip_paths, output_path) -> final reel path
#   - Uses ffmpeg concat demuxer
# - extract_clips_parallel(input_path, highlights, output_dir) -> list[clip_paths]
#   - Extract multiple clips in parallel using asyncio.gather()
#
# Note: All operations use local temp files