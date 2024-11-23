from app.domain.details.schemas import DetailCreateDTO, DetailDTO, DetailUpdateDTO
from app.utils.unitofwork import UnitOfWork


async def create(
    uow: UnitOfWork,
    dto: DetailCreateDTO,
) -> DetailDTO:
    id = await uow.details.create(**dto.model_dump())
    await uow.commit()
    model = await uow.details.get_by_id(id)
    return DetailDTO.model_validate(model)


async def update(
    uow: UnitOfWork,
    id: int,
    dto: DetailUpdateDTO,
) -> DetailDTO:
    await uow.details.update(id, **dto.model_dump(exclude_none=True))
    await uow.commit()
    model = await uow.details.get_by_id(id)
    return DetailDTO.model_validate(model)


async def delete(
    uow: UnitOfWork,
    id: int,
) -> None:
    await uow.details.delete(id)
    await uow.commit()
