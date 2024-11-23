from typing import Any

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import BaseModel


class BaseRepository[T: BaseModel]:
    model: type[T]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: int) -> T:
        stmt = select(self.model).filter_by(id=id)
        return (await self.session.execute(stmt)).scalar_one()

    async def get(self, **filters: dict[str, Any]) -> list[T]:
        stmt = select(self.model).filter_by(**filters)
        return list((await self.session.execute(stmt)).scalars().all())

    async def create(self, **data: dict[str, Any]) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        return (await self.session.execute(stmt)).scalar_one()

    async def update(self, id: int, **data: dict[str, Any]) -> None:
        stmt = update(self.model).values(**data).filter_by(id=id)
        await self.session.execute(stmt)

    async def delete(self, id: int) -> None:
        stmt = delete(self.model).filter_by(id=id)
        await self.session.execute(stmt)
