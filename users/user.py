from fastapi import APIRouter,Depends,HTTPException,status
from jupyterlab.utils import deprecated
from sqlalchemy.orm import Session
from config.settings import SessionLocal
from users import models
from passlib.context import CryptContext


pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')


router=APIRouter(prefix='/users',tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get():
    return {"message":"user bo'limi "}

@router.post("/register")
async def post():
    pass

    