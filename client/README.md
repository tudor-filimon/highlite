# Highlite Client

React frontend for the soccer highlight generator.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

The app will run on http://localhost:5173

## Features

- Drag & drop video upload
- Direct upload to Supabase (bypasses backend)
- Real-time processing status with progress stages
- Video player for viewing highlights
- Download functionality

## Structure

```
src/
├── main.jsx           # Entry point
├── App.jsx            # Main app component
├── index.css          # Global styles
├── App.css            # App styles
├── components/
│   ├── Header.jsx     # App header
│   ├── UploadSection.jsx  # Video upload form
│   ├── ProcessingStatus.jsx  # Processing progress
│   └── VideoPlayer.jsx    # Highlight player
└── services/
    └── api.js         # Backend API calls
```
