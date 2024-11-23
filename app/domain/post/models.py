from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import BaseModel
from app.domain.user.models import User


class Post(BaseModel):
    __tablename__ = 'posts'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]
    created_at: Mapped[datetime]

    user: Mapped[User] = relationship(lazy='selectin')
