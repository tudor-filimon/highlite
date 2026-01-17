# Highlite Server

FastAPI backend for soccer highlight reel generation using TwelveLabs.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy environment variables:
```bash
cp env.example .env
```

3. Fill in your `.env` file with:
   - Supabase URL and service key
   - TwelveLabs API key

4. Run the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload/init` | Get presigned URL for direct upload |
| POST | `/upload/complete` | Notify upload complete, start processing |
| GET | `/jobs/{id}/status` | Get processing status + progress |
| GET | `/jobs/{id}` | Get full job details |

## Architecture

```
app/
├── main.py          # FastAPI entry point
├── config.py        # Environment config
├── models.py        # Pydantic models
├── database.py      # Supabase client
├── routes/
│   ├── upload.py    # Upload endpoints
│   └── jobs.py      # Job status endpoints
├── services/
│   ├── storage.py   # Supabase Storage
│   ├── twelvelabs.py # TwelveLabs API
│   └── video.py     # FFmpeg operations
└── workers/
    └── processor.py # Background processing
```
