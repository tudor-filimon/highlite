# Autism Marker Detection API

FastAPI backend for psychologists to analyze child observation videos for autism behavioral markers using TwelveLabs AI.

## Setup

1. Install dependencies with uv:
```bash
uv sync
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
uv run uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload video, returns job_id |
| GET | `/jobs/{id}/status` | Get processing status + progress |
| GET | `/jobs/{id}/report` | Get JSON report with all markers |
| GET | `/jobs/{id}/clips` | List all detected marker clips |
| GET | `/jobs/{id}/clips/{index}` | Download specific clip |
| GET | `/health` | Health check |

## Output

### Report (JSON)
```json
{
  "job_id": "abc-123",
  "video_duration": 180.5,
  "analysis_date": "2024-01-15T10:30:00",
  "markers": [
    {
      "type": "hand_flapping",
      "start": 3.2,
      "end": 8.5,
      "confidence": 0.85,
      "description": "Child exhibits rapid hand flapping motion..."
    }
  ],
  "summary": "Analysis complete...",
  "marker_counts": {"hand_flapping": 2, "limited_eye_contact": 1},
  "total_markers": 3
}
```

### Clips
Individual video clips for each detected marker:
- `marker_000_hand_flapping_3.2s.mp4`
- `marker_001_limited_eye_contact_15.0s.mp4`

## Default Markers Detected

| Category | Markers |
|----------|---------|
| Motor | hand_flapping, rocking, spinning, toe_walking |
| Social | limited_eye_contact, lack_of_social_engagement |
| Communication | echolalia, limited_verbal_response |
| Sensory | covering_ears, unusual_sensory_response |
| Play | object_lining, repetitive_play |

## Architecture

```
POST /upload (video file)
    ↓
Save to temp directory
    ↓
Split into chunks (if > 15 min)
    ↓
TwelveLabs: Analyze for autism markers
    ↓
Extract individual clips with FFmpeg
    ↓
Generate report.json
    ↓
GET /report → JSON report
GET /clips/{n} → Download clip
```
