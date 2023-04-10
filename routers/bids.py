from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
import schemas, crud
import uuid
from ..main import get_db


router = APIRouter()


@router.post("/items/{item_id}/bid/", response_model=schemas.Bid)
def bid_item_for_user(
    item_id: uuid.UUID, bid: schemas.BidCreate, db: Session = Depends(get_db)
):
    return crud.bid_item(db=db, bid=bid, item_id=item_id)