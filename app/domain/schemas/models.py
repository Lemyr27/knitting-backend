from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.core.database import BaseModel
from app.domain.categories.models import Category
from app.domain.details.models import Detail


class Schema(BaseModel):
    __tablename__ = 'schemas'

    name: Mapped[str]
    description: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    details: Mapped[list[Detail]] = relationship(lazy='selectin')
    category:  Mapped[Category] = relationship(lazy='selectin')
