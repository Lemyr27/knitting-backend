from sqlalchemy.orm import Mapped

from app.core.database import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str]
