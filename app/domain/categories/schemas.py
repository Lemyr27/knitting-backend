from app.utils.schemas import BaseSchema


class CategoryBaseSchema(BaseSchema):
    name: str


class CategoryCreateDTO(CategoryBaseSchema):
    ...


class CategoryDTO(CategoryBaseSchema):
    id: int
