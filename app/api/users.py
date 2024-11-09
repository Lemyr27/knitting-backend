from app.domain.users import services
from app.domain.users.schemas import UserCreateDTO, UserDTO
from app.utils import dependencies


async def create_user(
    session: dependencies.db_session,
    dto: UserCreateDTO,
) -> UserDTO:
    result = await services.create(session, dto)
    return result


async def get_users(
    session: dependencies.db_session,
) -> list[UserDTO]:
    result = await services.get(session)
    return result
