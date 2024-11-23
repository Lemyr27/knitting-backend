from app.domain.schemas import services
from app.domain.schemas.schemas import SchemaCreateDTO, SchemaDTO, SchemaUpdateDTO
from app.utils import dependencies


async def get_schemas(
    uow: dependencies.uow,
) -> list[SchemaDTO]:
    result = await services.get(uow)
    return result


async def get_schema(
    uow: dependencies.uow,
    id: int,
) -> SchemaDTO:
    result = await services.get_one(uow, id)
    return result


async def create_schema(
    uow: dependencies.uow,
    _: dependencies.user,
    dto: SchemaCreateDTO,
) -> SchemaDTO:
    result = await services.create(uow, dto)
    return result


async def update_schema(
    uow: dependencies.uow,
    _: dependencies.user,
    id: int,
    dto: SchemaUpdateDTO,
) -> SchemaDTO:
    return await services.update(uow, id, dto)


async def delete_schema(
    uow: dependencies.uow,
    _: dependencies.user,
    id: int,
) -> None:
    await services.delete(uow, id)
