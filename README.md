# Highlite ⚽

AI-powered soccer highlight reel generator using TwelveLabs.

## Architecture

```
highlite/
├── client/          # React frontend (Vite)
└── server/          # FastAPI backend
```

## Quick Start

### 1. Backend Setup

```bash
cd server
pip install -r requirements.txt
cp env.example .env
# Edit .env with your Supabase and TwelveLabs credentials
uvicorn app.main:app --reload
```

### 2. Frontend Setup

```bash
cd client
npm install
npm run dev
```

### 3. Supabase Setup

Create a `videos` bucket in Supabase Storage and run this SQL:

```sql
-- Create jobs table
CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status VARCHAR(20) DEFAULT 'pending',
    progress INTEGER DEFAULT 0,
    keywords TEXT[],
    video_path TEXT,
    original_video_url TEXT,
    highlight_video_url TEXT,
    highlights_metadata JSONB,
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Make videos bucket public
UPDATE storage.buckets SET public = true WHERE name = 'videos';
```

## Flow

1. User uploads video directly to Supabase (presigned URL)
2. Backend splits video into 10-15 min chunks
3. All chunks analyzed in parallel by TwelveLabs (URL ingestion)
4. Highlights extracted and stitched into final reel
5. Original video + chunks deleted, only highlight reel kept

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: Python + FastAPI
- **Storage**: Supabase (Storage + PostgreSQL)
- **AI**: TwelveLabs API
- **Video**: FFmpeg
