# Environment variables configuration using pydantic-settings
#
# Settings:
# - twelvelabs_api_key: TwelveLabs API key
# - default_keywords: Default keywords if user doesn't provide any
# - chunk_duration_seconds: Duration of each video chunk (default 900 = 15 min)
# - chunk_overlap_seconds: Overlap between chunks (default 10 sec)
# - cors_origins: Allowed CORS origins
# - temp_dir: Directory for temporary files (default: system temp)
#
# Note: No Supabase needed - using local temp files and in-memory job tracking