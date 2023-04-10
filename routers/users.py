from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
import schemas, crud
import uuid
from ..main import get_db


router = APIRouter()


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
    
class UserInDB(schemas.User):
    hashed_password: str


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_telegram_id(db, telegram_id=user.TelegramUserId)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}/", response_model=schemas.User)
def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/telegram/{telegram_id}/", response_model=schemas.User)
def read_user_telegram(telegram_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_telegram_id(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user