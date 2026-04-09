from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models.account import Account
from src.models.transaction import Transaction, TransactionType
from src.models.user import User
from src.schemas.account import AccountCreate
from src.schemas.transaction import StatementResponse, TransactionCreate


async def create_account(payload: AccountCreate, user: User, db: AsyncSession) -> Account:
    result = await db.execute(select(Account).where(Account.number == payload.number))
    existing_account = result.scalar_one_or_none()

    if existing_account:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma conta com este número",
        )

    account = Account(number=payload.number, balance=Decimal("0.00"), user_id=user.id)
    db.add(account)
    await db.commit()
    await db.refresh(account)
    return account


async def get_user_account(account_id: int, user: User, db: AsyncSession) -> Account:
    result = await db.execute(
        select(Account)
        .where(Account.id == account_id, Account.user_id == user.id)
        .options(selectinload(Account.transactions))
    )
    account = result.scalar_one_or_none()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta nao encontrada",
        )

    return account


async def create_transaction(
    account_id: int,
    payload: TransactionCreate,
    user: User,
    db: AsyncSession,
) -> Transaction:
    account = await get_user_account(account_id=account_id, user=user, db=db)
    amount = payload.amount.quantize(Decimal("0.01"))

    if payload.type == TransactionType.WITHDRAW and account.balance < amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Saldo insuficiente para realizar o saque",
        )

    if payload.type == TransactionType.DEPOSIT:
        account.balance += amount
    else:
        account.balance -= amount

    transaction = Transaction(
        type=payload.type,
        amount=amount,
        description=payload.description,
        account_id=account.id,
    )

    db.add(transaction)
    db.add(account)
    await db.commit()
    await db.refresh(transaction)
    return transaction


async def get_statement(account_id: int, user: User, db: AsyncSession) -> StatementResponse:
    account = await get_user_account(account_id=account_id, user=user, db=db)
    return StatementResponse(
        account_id=account.id,
        account_number=account.number,
        balance=account.balance,
        transactions=account.transactions,
    )
