from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

from uuid import uuid4
from security.security import get_password_hash, verify_password

class UserIn(BaseModel):
    name: str
    id: str = Field(default_factory=lambda: str(uuid4()))
    password: str
    creation_time: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @validator("password", pre=True)
    def hash_password(cls, v):
        return get_password_hash(v)