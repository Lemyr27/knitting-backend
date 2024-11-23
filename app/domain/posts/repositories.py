from app.domain.posts.models import Post
from app.utils.repositories import BaseRepository


class PostRepository(BaseRepository[Post]):
    model = Post
