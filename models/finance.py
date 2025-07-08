# model.py

from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import Optional

from uuid import uuid4


class EarnIn(BaseModel):
    name: str
    id: str = Field(default_factory=lambda: str(uuid4()))
    amount: Decimal = Field(..., max_digits=10, decimal_places=2)
    way: str
    description: str | None = Field(default='Earn description')
    creation_time: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class ExpenseIn(BaseModel):
    name: str
    id: str = Field(default_factory=lambda: str(uuid4()))
    amount: Decimal = Field(..., max_digits=10, decimal_places=2)
    way: str
    description: str | None = Field(default='Expense description')
    creation_time: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class EarnUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[Decimal] = None
    way: Optional[str] = None
    description: Optional[str] = None
    
class ExpenseUpdate(EarnUpdate):
    pass
