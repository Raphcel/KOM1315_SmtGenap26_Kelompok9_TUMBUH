from sqlalchemy.orm import Session, joinedload

from app.domain.models.bookmark import Bookmark
from app.repositories.base import BaseRepository


class BookmarkRepository(BaseRepository[Bookmark]):
    """Repository for Bookmark entity — handles bookmark data access."""

    def __init__(self, db: Session):
        super().__init__(Bookmark, db)

    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> list[Bookmark]:
        """Retrieve all bookmarks for a user with opportunities eagerly loaded."""
        return (
            self._db.query(Bookmark)
            .options(joinedload(Bookmark.opportunity))
            .filter(Bookmark.user_id == user_id)
            .order_by(Bookmark.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_user_and_opportunity(self, user_id: int, opportunity_id: int) -> Bookmark | None:
        """Check if a user has bookmarked an opportunity."""
        return (
            self._db.query(Bookmark)
            .filter(
                Bookmark.user_id == user_id,
                Bookmark.opportunity_id == opportunity_id,
            )
            .first()
        )

    def count_by_user(self, user_id: int) -> int:
        """Count bookmarks for a user."""
        return (
            self._db.query(Bookmark)
            .filter(Bookmark.user_id == user_id)
            .count()
        )

    def delete_by_user_and_opportunity(self, user_id: int, opportunity_id: int) -> bool:
        """Remove a bookmark by user and opportunity."""
        bookmark = self.get_by_user_and_opportunity(user_id, opportunity_id)
        if bookmark:
            self._db.delete(bookmark)
            self._db.commit()
            return True
        return False
