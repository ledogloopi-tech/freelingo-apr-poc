from __future__ import annotations

from datetime import UTC, datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.review import Review
from app.models.user import User
from app.services.user_language_service import get_active_language


def _utcnow() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


async def get_user_review(db: AsyncSession, user_id: int) -> Review | None:
    result = await db.execute(select(Review).where(Review.user_id == user_id))
    return result.scalar_one_or_none()


async def create_review(
    db: AsyncSession,
    user: User,
    *,
    rating: int,
    comment: str | None,
) -> Review:
    existing = await get_user_review(db, user.id)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="review_already_exists")

    active_language = await get_active_language(db, user.id)
    target_language = active_language.target_language if active_language else user.target_language
    now = _utcnow()
    review = Review(
        user_id=user.id,
        user_display_name=user.display_name,
        target_language=target_language,
        rating=rating,
        comment=comment,
        is_approved=False,
        created_at=now,
        updated_at=now,
    )
    db.add(review)
    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="review_already_exists",
        ) from exc
    await db.refresh(review)
    return review


async def update_user_review(
    db: AsyncSession,
    user: User,
    *,
    rating: int,
    comment: str | None,
) -> Review:
    review = await get_user_review(db, user.id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="review_not_found")

    active_language = await get_active_language(db, user.id)
    review.user_display_name = user.display_name
    review.target_language = (
        active_language.target_language if active_language else user.target_language
    )
    review.rating = rating
    review.comment = comment
    review.is_approved = False
    review.updated_at = _utcnow()
    await db.commit()
    await db.refresh(review)
    return review


async def delete_user_review(db: AsyncSession, user_id: int) -> None:
    review = await get_user_review(db, user_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="review_not_found")
    await db.delete(review)
    await db.commit()


async def get_review_or_404(db: AsyncSession, review_id: int) -> Review:
    review = await db.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="review_not_found")
    return review


async def update_review_approval(
    db: AsyncSession,
    review_id: int,
    *,
    is_approved: bool,
) -> Review:
    review = await get_review_or_404(db, review_id)
    review.is_approved = is_approved
    review.updated_at = _utcnow()
    await db.commit()
    await db.refresh(review)
    return review


async def delete_review(db: AsyncSession, review_id: int) -> None:
    review = await get_review_or_404(db, review_id)
    await db.delete(review)
    await db.commit()
