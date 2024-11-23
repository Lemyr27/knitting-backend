from datetime import datetime

from app.domain.user.schemas import UserDTO
from app.utils.schemas import BaseSchema


class PostBaseSchema(BaseSchema):
    name: str
    description: str | None = None
    image: str | None = None


class PostCreateDTO(PostBaseSchema):
    ...


class PostUpdateDTO(BaseSchema):
    name: str | None = None
    description: str | None = None
    image: str | None = None


class PostDTO(PostBaseSchema):
    id: int
    user: UserDTO
    created_at: datetime
