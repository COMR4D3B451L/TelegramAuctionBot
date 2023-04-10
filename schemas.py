from pydantic import BaseModel
import uuid, datetime


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    images: str | None = None
    initial_price: int
    min_bid: int
    buy_now_price: int | None = None
    ends_at: datetime.datetime


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: uuid.UUID
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True