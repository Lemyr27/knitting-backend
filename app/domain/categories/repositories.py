from app.domain.categories.models import Category
from app.utils.repositories import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    model = Category
