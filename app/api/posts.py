from fastapi import HTTPException
from starlette import status

from app.domain.posts import services
from app.domain.posts.exceptions import CreatorCheckedException
from app.domain.posts.schemas import PostCreateDTO, PostDTO, PostUpdateDTO
from app.utils import dependencies


async def get_posts(
    uow: dependencies.uow,
) -> list[PostDTO]:
    result = await services.get(uow)
    return result


async def get_post(
    uow: dependencies.uow,
    id: int,
) -> PostDTO:
    result = await services.get_one(uow, id)
    return result


async def create_post(
    uow: dependencies.uow,
    user: dependencies.user,
    dto: PostCreateDTO,
) -> PostDTO:
    result = await services.create(uow, user, dto)
    return result


async def update_post(
    uow: dependencies.uow,
    user: dependencies.user,
    id: int,
    dto: PostUpdateDTO,
) -> PostDTO:
    try:
        return await services.update(uow, user, id, dto)
    except CreatorCheckedException as e:
        raise HTTPException(status.HTTP_403_FORBIDDEN, e.message)


async def delete_post(
    uow: dependencies.uow,
    user: dependencies.user,
    id: int,
) -> None:
    try:
        await services.delete(uow, user, id)
    except CreatorCheckedException as e:
        raise HTTPException(status.HTTP_403_FORBIDDEN, e.message)
