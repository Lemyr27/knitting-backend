from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.users.models import User
from app.domain.users.schemas import UserCreateDTO, UserDTO


async def create(
    session: AsyncSession,
    dto: UserCreateDTO,
) -> UserDTO:
    data = dto.model_dump()
    stmt = insert(User).values(**data).returning(User.id)
    id = (await session.execute(stmt)).scalar_one()
    await session.commit()
    model = await session.get_one(User, id)
    return UserDTO.model_validate(model)


async def get(
    session: AsyncSession,
) -> list[UserDTO]:
    stmt = select(User)
    result = list((await session.execute(stmt)).scalars().all())
    return [UserDTO.model_validate(u) for u in result]
