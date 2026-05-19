from sqlalchemy.orm import Session

from app.domain.models.externship import Externship
from app.repositories.base import BaseRepository


class ExternshipRepository(BaseRepository[Externship]):
    """Repository for Externship entity — handles externship data access."""

    def __init__(self, db: Session):
        super().__init__(Externship, db)

    def get_by_student(self, student_id: int, skip: int = 0, limit: int = 100) -> list[Externship]:
        """Retrieve all externships for a student."""
        return (
            self._db.query(Externship)
            .filter(Externship.student_id == student_id)
            .order_by(Externship.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def count_by_student(self, student_id: int) -> int:
        """Count externships for a student."""
        return (
            self._db.query(Externship)
            .filter(Externship.student_id == student_id)
            .count()
        )
