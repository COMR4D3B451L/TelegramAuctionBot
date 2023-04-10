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
    username: str
    TelegramUserId: str
    is_seller: bool = False


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: uuid.UUID
    items: list[Item] = []

    class Config:
        orm_mode = True


class BidBase(BaseModel):
    amount: int
    timestamp: datetime.datetime
   

class BidCreate(BidBase):
    pass


class Bid(BidBase):
    id: uuid.UUID
    user_id: uuid.UUID
    item_id: uuid.UUID
    
    class Config:
        orm_mode = True