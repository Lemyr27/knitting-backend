from app.domain.schemas.models import Schema
from app.utils.repositories import BaseRepository


class SchemaRepository(BaseRepository[Schema]):
    model = Schema
