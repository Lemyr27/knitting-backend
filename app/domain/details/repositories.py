from app.domain.details.models import Detail
from app.utils.repositories import BaseRepository


class DetailRepository(BaseRepository[Detail]):
    model = Detail
