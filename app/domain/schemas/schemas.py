from app.domain.details.schemas import DetailDTO
from app.utils.schemas import BaseSchema


class SchemaBaseSchema(BaseSchema):
    name: str
    description: str | None = None


class SchemaCreateDTO(SchemaBaseSchema):
    ...


class SchemaUpdateDTO(BaseSchema):
    name: str | None = None
    description: str | None = None


class SchemaDTO(SchemaBaseSchema):
    id: int
    details: list[DetailDTO]
