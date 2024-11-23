from fastapi import APIRouter

from app.api.post import get_posts, get_post, create_post, update_post, delete_post

router = APIRouter(prefix='/posts', tags=['posts'])

router.add_api_route('', get_posts, methods=['GET'])
router.add_api_route('/{id}', get_post, methods=['GET'])
router.add_api_route('', create_post, methods=['POST'])
router.add_api_route('/{id}', update_post, methods=['PATCH'])
router.add_api_route('/{id}', delete_post, methods=['DELETE'])
