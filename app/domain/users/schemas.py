from pydantic import Field, EmailStr

from app.utils.schemas import BaseSchema


class UserBaseSchema(BaseSchema):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)


class UserCreateDTO(UserBaseSchema):
    email: EmailStr
    avatar_color: str


class UserLoginDTO(UserBaseSchema):
    ...


class UserDTO(BaseSchema):
    id: int
    username: str
    email: EmailStr
    avatar_color: str


class TokenDTO(BaseSchema):
    access_token: str
    token_type: str
