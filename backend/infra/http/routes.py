from fastapi import APIRouter, Depends, Body
from typing import Annotated, Callable

from domain.sentiaspect_evaluation import AspectRating

from infra.http.dependencies import get_sentiaspect_evaluator

router = APIRouter()

@router.post("/")
async def root(
    text: Annotated[str, Body(description="Текст отзыва")],
    sentiaspect_evaluator: Annotated[
        Callable[[str], AspectRating],
        Depends(get_sentiaspect_evaluator),
    ]
) -> AspectRating:
    """
    Аспектно-сентиментный анализ отзыва.
    """
    return sentiaspect_evaluator(text)
