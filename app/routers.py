from fastapi import APIRouter

from app.api.users import get_users, create_user

router = APIRouter(prefix='/api/v1/user', tags=['user'])

router.add_api_route('', create_user, methods=['POST'])
router.add_api_route('', get_users, methods=['GET'])
