from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schemas.auth import TokenResponse, UserLogin, UserRegister
from src.schemas.user import UserResponse
from src.services.auth_service import authenticate_user, register_user

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar usuário",
    description="Cria um novo usuário para autenticação na API.",
)
async def register(payload: UserRegister, db: AsyncSession = Depends(get_db)) -> UserResponse:
    user = await register_user(payload=payload, db=db)
    return user


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Autenticar usuário",
    description="Autentica um usuário e retorna um token JWT.",
)
async def login(payload: UserLogin, db: AsyncSession = Depends(get_db)) -> TokenResponse:
    access_token = await authenticate_user(payload=payload, db=db)
    return TokenResponse(access_token=access_token)
