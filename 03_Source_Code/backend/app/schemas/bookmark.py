from datetime import datetime
from pydantic import BaseModel

from app.schemas.opportunity import OpportunityResponse


# ── Request Schemas ──────────────────────────────────────────

class BookmarkCreate(BaseModel):
    """Schema for bookmarking an opportunity."""
    opportunity_id: int


# ── Response Schemas ─────────────────────────────────────────

class BookmarkResponse(BaseModel):
    """Schema for bookmark data in API responses."""
    id: int
    user_id: int
    opportunity_id: int
    created_at: datetime
    opportunity: OpportunityResponse | None = None

    class Config:
        from_attributes = True


class BookmarkListResponse(BaseModel):
    """Paginated bookmark list response."""
    items: list[BookmarkResponse]
    total: int
