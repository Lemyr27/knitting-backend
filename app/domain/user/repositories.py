from sqlalchemy import select

from app.domain.user.models import User
from app.utils.repositories import BaseRepository


class UserRepository(BaseRepository[User]):
    model = User

    async def get_user_by_name(self, username: str) -> User:
        stmt = select(User).filter_by(username=username).limit(1)
        return (await self.session.execute(stmt)).scalar_one()
