from fastapi import APIRouter

from app.api.categories import delete_category, create_category, get_categories

router = APIRouter(prefix='/categories', tags=['categories'])

router.add_api_route('', get_categories, methods=['GET'])
router.add_api_route('', create_category, methods=['POST'])
router.add_api_route('/{id}', delete_category, methods=['DELETE'])
