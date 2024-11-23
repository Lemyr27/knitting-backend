from app.domain.schemas.schemas import SchemaCreateDTO, SchemaDTO, SchemaUpdateDTO
from app.utils.unitofwork import UnitOfWork


async def get(uow: UnitOfWork) -> list[SchemaDTO]:
    return [SchemaDTO.model_validate(s) for s in await uow.schemas.get()]


async def get_one(uow: UnitOfWork, id: int) -> SchemaDTO:
    model = await uow.schemas.get_by_id(id)
    return SchemaDTO.model_validate(model)


async def create(
    uow: UnitOfWork,
    dto: SchemaCreateDTO,
) -> SchemaDTO:
    id = await uow.schemas.create(**dto.model_dump())
    await uow.commit()
    model = await uow.schemas.get_by_id(id)
    return SchemaDTO.model_validate(model)


async def update(
    uow: UnitOfWork,
    id: int,
    dto: SchemaUpdateDTO,
) -> SchemaDTO:
    await uow.schemas.update(id, **dto.model_dump(exclude_none=True))
    await uow.commit()
    model = await uow.schemas.get_by_id(id)
    return SchemaDTO.model_validate(model)


async def delete(
    uow: UnitOfWork,
    id: int,
) -> None:
    await uow.schemas.delete(id)
    await uow.commit()
