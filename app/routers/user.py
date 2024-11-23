from fastapi import APIRouter

from app.api.user import create_user, login, get_me

router = APIRouter(prefix='/users', tags=['users'])

router.add_api_route('', create_user, methods=['POST'])
router.add_api_route('/token', login, methods=['POST'])
router.add_api_route('/me', get_me, methods=['GET'])
