from app.utils.schemas import BaseSchema


class DetailBaseSchema(BaseSchema):
    name: str
    details_number: int
    rows_number: int
    schema_text: str | None = None
    schema_image: str | None = None


class DetailCreateDTO(DetailBaseSchema):
    schema_id: int


class DetailUpdateDTO(BaseSchema):
    name: str | None = None
    details_number: int | None = None
    rows_number: int | None = None
    schema_text: str | None = None
    schema_image: str | None = None


class DetailDTO(DetailBaseSchema):
    id: int
