# FastAPI application entry point
#
# - Create FastAPI app with title, description, version
# - Add CORS middleware with origins from config
# - Include routers:
#   - /upload (upload.router)
#   - /jobs (jobs.router)
# - Add /health endpoint for health checks
#
# Note: No database connection needed - using in-memory job store