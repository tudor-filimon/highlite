from pydantic import BaseModel
from typing import Optional
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


# Response models
class UploadResponse(BaseModel):
    job_id: str
    status: JobStatus
    message: str


class JobStatusResponse(BaseModel):
    job_id: str
    status: JobStatus
    progress: int
    error_message: Optional[str] = None


# Marker model - detected autism behavioral marker
class MarkerResponse(BaseModel):
    type: str  # "hand_flapping", "limited_eye_contact", etc.
    start: float  # Start timestamp in seconds
    end: float  # End timestamp in seconds
    confidence: float  # 0.0 - 1.0
    description: str  # AI-generated description


# Report model - full analysis report
class ReportResponse(BaseModel):
    job_id: str
    video_duration: float
    analysis_date: datetime
    markers: list[MarkerResponse]
    summary: str  # Overall AI summary
    marker_counts: dict[str, int]  # {"hand_flapping": 3, ...}
    total_markers: int


# Clip info model
class ClipInfo(BaseModel):
    index: int
    marker_type: str
    start: float
    end: float
    filename: str


class ClipsListResponse(BaseModel):
    job_id: str
    total_clips: int
    clips: list[ClipInfo]


# Internal job model (stored in memory)
@dataclass
class Job:
    id: str
    status: JobStatus = JobStatus.PENDING
    progress: int = 0
    markers: list[str] = field(default_factory=list)  # Markers to look for
    video_path: Optional[str] = None
    report_path: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


# Internal marker model
@dataclass
class Marker:
    type: str
    start: float
    end: float
    confidence: float
    description: str
