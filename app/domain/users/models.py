from sqlalchemy.orm import Mapped

from app.core.database import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    avatar_color: Mapped[str]
