from app.domain.categories.schemas import CategoryDTO
from app.domain.details.schemas import DetailDTO
from app.utils.schemas import BaseSchema


class SchemaBaseSchema(BaseSchema):
    name: str
    description: str | None = None


class SchemaCreateDTO(SchemaBaseSchema):
    category_id: int


class SchemaUpdateDTO(BaseSchema):
    name: str | None = None
    category_id: int | None = None
    description: str | None = None


class SchemaDTO(SchemaBaseSchema):
    id: int
    category: CategoryDTO | None
    details: list[DetailDTO]
