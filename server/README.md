# Highlite Server

FastAPI backend for soccer highlight reel generation using TwelveLabs.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install FFmpeg (required for video processing):
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

3. Copy environment variables:
```bash
cp env.example .env
```

4. Add your TwelveLabs API key to `.env`

5. Run the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload video file + keywords, returns job_id |
| GET | `/jobs/{id}/status` | Get processing status + progress |
| GET | `/jobs/{id}/download` | Download the highlight reel |

## Architecture (Simplified for Hackathon)

- **No database** - Jobs stored in memory dict
- **No cloud storage** - Files in local temp directory
- **Direct TwelveLabs upload** - No URL ingestion needed

```
POST /upload
  → Save to /tmp/highlite/{job_id}/original.mp4
  → Start background processing
  → Return job_id

Background Processing:
  → Split video into chunks
  → Upload each chunk to TwelveLabs (parallel)
  → Get highlight timestamps
  → Extract + stitch clips with FFmpeg
  → Save to /tmp/highlite/{job_id}/highlight_reel.mp4

GET /jobs/{id}/download
  → Stream highlight_reel.mp4 to user
```

## File Structure

```
/tmp/highlite/{job_id}/
├── original.mp4        # Uploaded video (deleted after processing)
├── chunks/             # Split chunks (deleted after processing)
├── clips/              # Extracted clips (deleted after processing)
└── highlight_reel.mp4  # Final output (kept until download)
```
