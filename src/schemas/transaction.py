from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.models.transaction import TransactionType


class TransactionCreate(BaseModel):
    type: TransactionType = Field(..., description="Tipo da transação: deposit ou withdraw")
    amount: Decimal = Field(..., gt=0, description="Valor da transação")
    description: str | None = Field(None, max_length=255, description="Descrição opcional")

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: Decimal) -> Decimal:
        if value <= 0:
            raise ValueError("O valor da transacao deve ser maior que zero")
        return value.quantize(Decimal("0.01"))


class TransactionResponse(BaseModel):
    id: int
    type: TransactionType
    amount: Decimal
    description: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class StatementResponse(BaseModel):
    account_id: int
    account_number: str
    balance: Decimal
    transactions: list[TransactionResponse]
