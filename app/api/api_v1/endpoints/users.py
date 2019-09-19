from fastapi import APIRouter

from app.models.user import User

router = APIRouter()


@router.get("/", response_model=User)
async def get_user():
    user = {"id": "12312312", "name": "Xico"}
    return User(**user)
