from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
import schemas, crud
import uuid
from ..main import get_db
from typing import List


router = APIRouter()

@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: uuid.UUID, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/{item_id}/", response_model=List[schemas.Item])
def read_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item