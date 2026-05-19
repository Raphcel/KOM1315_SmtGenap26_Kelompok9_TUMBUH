from fastapi import APIRouter, Depends, Query

from app.domain.models.user import User
from app.services.externship_service import ExternshipService
from app.schemas.externship import (
    ExternshipCreate, ExternshipUpdate, ExternshipResponse, ExternshipListResponse,
)
from app.api.dependencies import get_externship_service, get_current_user, require_role

router = APIRouter(prefix="/externships", tags=["Externships"])


@router.post("/", response_model=ExternshipResponse, status_code=201)
def create_externship(
    data: ExternshipCreate,
    current_user: User = Depends(require_role("student")),
    externship_service: ExternshipService = Depends(get_externship_service),
):
    """Create a new externship record (student only)."""
    return externship_service.create_externship(current_user.id, data)


@router.get("/me", response_model=ExternshipListResponse)
def my_externships(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    current_user: User = Depends(require_role("student")),
    externship_service: ExternshipService = Depends(get_externship_service),
):
    """List all externships for the current student."""
    return externship_service.get_student_externships(current_user.id, skip, limit)


@router.put("/{externship_id}", response_model=ExternshipResponse)
def update_externship(
    externship_id: int,
    data: ExternshipUpdate,
    current_user: User = Depends(require_role("student")),
    externship_service: ExternshipService = Depends(get_externship_service),
):
    """Update an externship record (student only, own records)."""
    return externship_service.update_externship(externship_id, current_user.id, data)


@router.delete("/{externship_id}", status_code=204)
def delete_externship(
    externship_id: int,
    current_user: User = Depends(require_role("student")),
    externship_service: ExternshipService = Depends(get_externship_service),
):
    """Delete an externship record (student only, own records)."""
    externship_service.delete_externship(externship_id, current_user.id)
