from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class AccountCreate(BaseModel):
    number: str = Field(..., min_length=4, max_length=20, description="Número da conta")


class AccountResponse(BaseModel):
    id: int
    number: str
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)
