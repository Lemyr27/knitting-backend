from sqlalchemy.orm import Mapped, relationship

from app.core.database import BaseModel
from app.domain.details.models import Detail


class Schema(BaseModel):
    __tablename__ = 'schemas'

    name: Mapped[str]
    description: Mapped[str]

    details: Mapped[list[Detail]] = relationship(lazy='selectin')
