from app.domain.categories.schemas import CategoryCreateDTO, CategoryDTO
from app.utils.unitofwork import UnitOfWork


async def get(uow: UnitOfWork) -> list[CategoryDTO]:
    return [CategoryDTO.model_validate(p) for p in await uow.categories.get()]


async def create(
    uow: UnitOfWork,
    dto: CategoryCreateDTO,
) -> CategoryDTO:
    id = await uow.categories.create(**dto.model_dump())
    await uow.commit()
    model = await uow.categories.get_by_id(id)
    return CategoryDTO.model_validate(model)


async def delete(
    uow: UnitOfWork,
    id: int,
) -> None:
    await uow.categories.delete(id)
    await uow.commit()
