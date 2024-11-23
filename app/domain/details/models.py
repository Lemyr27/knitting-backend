from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import BaseModel


class Detail(BaseModel):
    __tablename__ = 'details'

    schema_id: Mapped[int] = mapped_column(ForeignKey('schemas.id'))
    name: Mapped[str]
    details_number: Mapped[int]
    rows_number: Mapped[int]
    schema_text: Mapped[str]
    schema_image: Mapped[str]
