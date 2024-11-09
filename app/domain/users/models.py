from sqlalchemy.orm import Mapped

from app.core.database import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name: Mapped[str]
    email: Mapped[str]
