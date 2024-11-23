from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.core.settings import app_settings
from app.domain.user.exceptions import CredentialsValidateException
from app.domain.user.schemas import UserDTO
from app.utils.unitofwork import UnitOfWork, unit_of_work

_bearer = HTTPBearer(scheme_name='bearer')
_token = Annotated[HTTPAuthorizationCredentials, Depends(_bearer)]

db_session = Annotated[AsyncSession, Depends(get_db_session)]
uow = Annotated[UnitOfWork, Depends(unit_of_work)]


async def get_current_user(
    uow: uow,
    token: _token,
) -> UserDTO:
    payload = jwt.decode(token.credentials, app_settings.SECRET_KEY, algorithms=[app_settings.ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
        raise CredentialsValidateException()

    model = await uow.users.get_user_by_name(username)
    return UserDTO.model_validate(model)


user = Annotated[UserDTO, Depends(get_current_user)]
