from app.domain.categories import services
from app.domain.categories.schemas import CategoryCreateDTO, CategoryDTO
from app.utils import dependencies


async def get_categories(
    uow: dependencies.uow,
) -> list[CategoryDTO]:
    result = await services.get(uow)
    return result


async def create_category(
    uow: dependencies.uow,
    dto: CategoryCreateDTO,
) -> CategoryDTO:
    result = await services.create(uow, dto)
    return result


async def delete_category(
    uow: dependencies.uow,
    id: int,
) -> None:
    await services.delete(uow, id)
