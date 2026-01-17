// API service for backend communication

const API_BASE = '/api'

// POST /upload/init - Get presigned URL for direct upload
export async function initUpload(filename, keywords = []) {
  // TODO: Implement
}

// Upload directly to Supabase using presigned URL
export async function uploadToSupabase(uploadUrl, file, onProgress) {
  // TODO: Implement with XMLHttpRequest for progress tracking
}

// POST /upload/complete - Notify backend upload is done
export async function completeUpload(jobId) {
  // TODO: Implement
}

// GET /jobs/{id}/status - Poll for processing status
export async function getJobStatus(jobId) {
  // TODO: Implement
}
