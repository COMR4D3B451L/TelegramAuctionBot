from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
import uuid, os, datetime


app = FastAPI()




@app.get("/")
async def root():
    return {"message": "this is coming from an API"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
