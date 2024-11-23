from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from app.core.settings import app_settings
from app.domain.users.exceptions import IncorrectUsernameOrPasswordException
from app.domain.users.schemas import UserDTO, UserCreateDTO, TokenDTO, UserLoginDTO
from app.utils.unitofwork import UnitOfWork


async def login(
    uow: UnitOfWork,
    dto: UserLoginDTO,
) -> TokenDTO:
    user = await uow.users.get_user_by_name(dto.username)
    if not bcrypt.checkpw(dto.password.encode(), user.password.encode()):
        raise IncorrectUsernameOrPasswordException()

    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode = {"sub": user.username, "exp": expire}
    access_token = jwt.encode(to_encode, app_settings.SECRET_KEY, app_settings.ALGORITHM)
    return TokenDTO(access_token=access_token, token_type="Bearer")


async def create(
    uow: UnitOfWork,
    dto: UserCreateDTO,
) -> UserDTO:
    dto.password = bcrypt.hashpw(dto.password.encode(), bcrypt.gensalt()).decode()
    id = await uow.users.create(**dto.model_dump())
    await uow.commit()
    model = await uow.users.get_by_id(id)
    return UserDTO.model_validate(model)
