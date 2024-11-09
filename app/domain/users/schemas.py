from app.utils.schemas import BaseSchema


class UserBase(BaseSchema):
    name: str
    email: str


class UserCreateDTO(UserBase):
    ...


class UserUpdateDTO(UserBase):
    ...


class UserDTO(UserBase):
    id: int
