from app.domain.details import services
from app.domain.details.schemas import DetailCreateDTO, DetailDTO, DetailUpdateDTO
from app.utils import dependencies


async def create_detail(
    uow: dependencies.uow,
    _: dependencies.user,
    dto: DetailCreateDTO,
) -> DetailDTO:
    result = await services.create(uow, dto)
    return result


async def update_detail(
    uow: dependencies.uow,
    _: dependencies.user,
    id: int,
    dto: DetailUpdateDTO,
) -> DetailDTO:
    return await services.update(uow, id, dto)


async def delete_detail(
    uow: dependencies.uow,
    _: dependencies.user,
    id: int,
) -> None:
    await services.delete(uow, id)
