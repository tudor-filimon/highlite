# Highlite - Autism Marker Detection

AI-powered tool for psychologists to analyze child observation videos for autism behavioral markers.

## Quick Start

### Backend
```bash
cd server
uv sync
cp env.example .env
# Add your TWELVELABS_API_KEY to .env
uv run uvicorn app.main:app --reload
```

### Frontend
```bash
cd client
npm install
npm run dev
```

## What It Does

1. **Upload** - Psychologist uploads video of child observation session
2. **Analyze** - TwelveLabs AI detects autism behavioral markers
3. **Report** - Get JSON report with timestamps and descriptions
4. **Clips** - Download individual video clips of each detected marker

## Markers Detected

- Hand flapping, rocking, spinning, toe walking
- Limited eye contact, lack of social engagement
- Echolalia, limited verbal response
- Covering ears, unusual sensory responses
- Object lining, repetitive play patterns

## API

| Endpoint | Description |
|----------|-------------|
| `POST /upload` | Upload video for analysis |
| `GET /jobs/{id}/status` | Check processing progress |
| `GET /jobs/{id}/report` | Get analysis report (JSON) |
| `GET /jobs/{id}/clips` | List detected marker clips |
| `GET /jobs/{id}/clips/{n}` | Download specific clip |

## Tech Stack

- **Backend**: Python + FastAPI + uv
- **AI**: TwelveLabs API
- **Video**: FFmpeg
- **Storage**: Local temp files (no cloud needed)
