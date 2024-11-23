from typing import Any

from app.core.database import async_session
from app.domain.post.repositories import PostRepository
from app.domain.user.repositories import UserRepository


class UnitOfWork:
    async def __aenter__(self):
        self.session = async_session()

        self.users = UserRepository(self.session)
        self.posts = PostRepository(self.session)
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
