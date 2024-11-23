from app.domain.post.exceptions import CreatorCheckedException
from app.domain.post.schemas import PostCreateDTO, PostDTO, PostUpdateDTO
from app.domain.user.schemas import UserDTO
from app.utils.unitofwork import UnitOfWork


async def get(uow: UnitOfWork) -> list[PostDTO]:
    return [PostDTO.model_validate(p) for p in await uow.posts.get()]


async def get_one(uow: UnitOfWork, id: int) -> PostDTO:
    model = await uow.posts.get_by_id(id)
    return PostDTO.model_validate(model)


async def create(
    uow: UnitOfWork,
    user: UserDTO,
    dto: PostCreateDTO,
) -> PostDTO:
    data = dto.model_dump()
    data['user_id'] = user.id
    id = await uow.posts.create(**data)
    await uow.commit()
    model = await uow.posts.get_by_id(id)
    return PostDTO.model_validate(model)


async def update(
    uow: UnitOfWork,
    user: UserDTO,
    id: int,
    dto: PostUpdateDTO,
) -> PostDTO:
    model = await uow.posts.get_by_id(id)
    if model.user_id != user.id:
        raise CreatorCheckedException()

    await uow.posts.update(id, **dto.model_dump(exclude_none=True))
    await uow.commit()
    await uow.refresh(model)
    return PostDTO.model_validate(model)


async def delete(
    uow: UnitOfWork,
    user: UserDTO,
    id: int,
) -> None:
    model = await uow.posts.get_by_id(id)
    if model.user_id != user.id:
        raise CreatorCheckedException()

    await uow.posts.delete(id)
    await uow.commit()
