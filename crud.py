from sqlalchemy.orm import Session
import models, schemas
import uuid


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_telegram_id(db: Session, telegram_id: str):
    return db.query(models.User).filter(models.User.telegram_id == telegram_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, telegram_id=user.TelegramUserId)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: uuid.UUID):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def bid_item(db: Session, bid: schemas.BidCreate, user_id: uuid.UUID, item_id: uuid.UUID):
    db_bid = models.Bid(**bid.dict(), user_id=user_id, item_id=item_id)
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid