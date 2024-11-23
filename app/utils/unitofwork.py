from typing import Any

from app.core.database import async_session
from app.domain.details.repositories import DetailRepository
from app.domain.posts.repositories import PostRepository
from app.domain.users.repositories import UserRepository
from app.domain.schemas.repositories import SchemaRepository


class UnitOfWork:
    async def __aenter__(self):
        self.session = async_session()

        self.users = UserRepository(self.session)
        self.posts = PostRepository(self.session)
        self.schemas = SchemaRepository(self.session)
        self.details = DetailRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def refresh(self, obj: Any) -> None:
        await self.session.refresh(obj)


async def unit_of_work() -> UnitOfWork:
    async with UnitOfWork() as uow:
        yield uow
