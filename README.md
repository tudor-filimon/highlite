# Highlite

AI-powered soccer highlight reel generator using TwelveLabs.

## Architecture (Simplified for Hackathon)

```
┌─────────────────────────────────────────────────────────────────┐
│                         NO EXTERNAL STORAGE                     │
│                                                                 │
│   • Jobs stored in memory (Python dict)                         │
│   • Files stored in local /tmp directory                        │
│   • Direct file upload to TwelveLabs (no URL ingestion)         │
│   • Highlight reel returned as direct download                  │
└─────────────────────────────────────────────────────────────────┘
```

```
User ──upload──> Backend ──file upload──> TwelveLabs
                    │                          │
                    │                     timestamps
                    │                          │
                    ◄──────────────────────────┘
                    │
               FFmpeg (extract + stitch)
                    │
                    ▼
              highlight_reel.mp4
                    │
User <──download────┘
```

## Quick Start

### Backend
```bash
cd server
pip install -r requirements.txt
cp env.example .env
# Add your TWELVELABS_API_KEY to .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd client
npm install
npm run dev
```

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload video + keywords, returns job_id |
| GET | `/jobs/{id}/status` | Poll for status + progress |
| GET | `/jobs/{id}/download` | Download highlight reel |

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: Python + FastAPI
- **AI**: TwelveLabs API
- **Video**: FFmpeg
- **Storage**: Local temp files (no cloud needed)
