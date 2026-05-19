from fastapi import APIRouter, Depends

from app.domain.models.user import User
from app.services.bookmark_service import BookmarkService
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkListResponse
from app.api.dependencies import get_bookmark_service, get_current_user, require_role

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])


@router.post("/", response_model=BookmarkResponse, status_code=201)
def add_bookmark(
    data: BookmarkCreate,
    current_user: User = Depends(require_role("student")),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
):
    """Save an opportunity to bookmarks (student only)."""
    return bookmark_service.add_bookmark(current_user.id, data)


@router.delete("/{opportunity_id}", status_code=204)
def remove_bookmark(
    opportunity_id: int,
    current_user: User = Depends(require_role("student")),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
):
    """Remove an opportunity from bookmarks (student only)."""
    bookmark_service.remove_bookmark(current_user.id, opportunity_id)


@router.get("/me", response_model=BookmarkListResponse)
def my_bookmarks(
    current_user: User = Depends(require_role("student")),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
):
    """List all bookmarked opportunities for the current student."""
    return bookmark_service.get_user_bookmarks(current_user.id)


@router.get("/check/{opportunity_id}")
def check_bookmark(
    opportunity_id: int,
    current_user: User = Depends(require_role("student")),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
):
    """Check if an opportunity is bookmarked by the current student."""
    return {"bookmarked": bookmark_service.is_bookmarked(current_user.id, opportunity_id)}
