from fastapi import FastAPI, HTTPException
from jwt import DecodeError
from sqlalchemy.exc import NoResultFound
from starlette import status

from app.domain.user import services
from app.domain.user.exceptions import CredentialsValidateException, IncorrectUsernameOrPasswordException
from app.domain.user.schemas import UserCreateDTO, UserDTO, TokenDTO, UserLoginDTO
from app.utils import dependencies


async def create_user(
    uow: dependencies.uow,
    dto: UserCreateDTO,
) -> UserDTO:
    return await services.create(uow, dto)


async def login(
    uow: dependencies.uow,
    dto: UserLoginDTO,
) -> TokenDTO:
    try:
        return await services.login(uow, dto)
    except IncorrectUsernameOrPasswordException as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.message)
    except NoResultFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Incorrect username or password')


async def get_me(
    user: dependencies.user,
) -> UserDTO:
    try:
        return user
    except CredentialsValidateException as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.message)
    except DecodeError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Invalid token')
