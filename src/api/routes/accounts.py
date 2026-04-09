from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.dependencies.auth import get_current_user
from src.models.user import User
from src.schemas.account import AccountCreate, AccountResponse
from src.schemas.transaction import StatementResponse, TransactionCreate, TransactionResponse
from src.services.account_service import create_account, create_transaction, get_statement

router = APIRouter(prefix="/accounts", tags=["Contas"])


@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar conta corrente",
    description="Cria uma conta corrente vinculada ao usuário autenticado.",
)
async def create_new_account(
    payload: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> AccountResponse:
    account = await create_account(payload=payload, user=current_user, db=db)
    return account


@router.post(
    "/{account_id}/transactions",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar transação",
    description="Registra depósito ou saque em uma conta do usuário autenticado.",
)
async def create_account_transaction(
    account_id: int,
    payload: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> TransactionResponse:
    transaction = await create_transaction(
        account_id=account_id,
        payload=payload,
        user=current_user,
        db=db,
    )
    return transaction


@router.get(
    "/{account_id}/statement",
    response_model=StatementResponse,
    summary="Consultar extrato",
    description="Exibe o extrato completo da conta, incluindo saldo e transações.",
)
async def get_account_statement(
    account_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> StatementResponse:
    return await get_statement(account_id=account_id, user=current_user, db=db)
