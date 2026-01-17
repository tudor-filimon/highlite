// API service for backend communication

const API_BASE = '/api'

// POST /upload - Upload video file directly to backend
export async function uploadVideo(file, keywords = [], onProgress) {
  // TODO: Implement with FormData
  // - file: video file
  // - keywords: optional array of keywords
  // - onProgress: callback for upload progress
  // Returns: { job_id }
}

// GET /jobs/{id}/status - Poll for processing status
export async function getJobStatus(jobId) {
  // TODO: Implement
  // Returns: { job_id, status, progress, error_message }
}

// GET /jobs/{id}/download - Download highlight reel
export function getDownloadUrl(jobId) {
  return `${API_BASE}/jobs/${jobId}/download`
}
