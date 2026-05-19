from fastapi import HTTPException, status

from app.repositories.bookmark_repository import BookmarkRepository
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkListResponse


class BookmarkService:
    """Service handling bookmark business logic."""

    def __init__(self, bookmark_repo: BookmarkRepository):
        self._bookmark_repo = bookmark_repo

    def add_bookmark(self, user_id: int, data: BookmarkCreate) -> BookmarkResponse:
        """Bookmark an opportunity."""
        existing = self._bookmark_repo.get_by_user_and_opportunity(
            user_id, data.opportunity_id
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already bookmarked this opportunity",
            )

        bookmark = self._bookmark_repo.create({
            "user_id": user_id,
            "opportunity_id": data.opportunity_id,
        })
        return BookmarkResponse.model_validate(bookmark)

    def remove_bookmark(self, user_id: int, opportunity_id: int) -> dict:
        """Remove a bookmark."""
        success = self._bookmark_repo.delete_by_user_and_opportunity(user_id, opportunity_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bookmark not found",
            )
        return {"message": "Bookmark removed successfully"}

    def get_user_bookmarks(
        self, user_id: int, skip: int = 0, limit: int = 100
    ) -> BookmarkListResponse:
        """List all bookmarks for a user."""
        bookmarks = self._bookmark_repo.get_by_user(user_id, skip, limit)
        total = self._bookmark_repo.count_by_user(user_id)
        return BookmarkListResponse(
            items=[BookmarkResponse.model_validate(b) for b in bookmarks],
            total=total,
        )

    def is_bookmarked(self, user_id: int, opportunity_id: int) -> bool:
        """Check if a user has bookmarked an opportunity."""
        return self._bookmark_repo.get_by_user_and_opportunity(user_id, opportunity_id) is not None
