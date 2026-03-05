from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import register_user, login_user, get_users
from app.schemas import UserCreate, UserLogin

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.name, user.email, user.password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user(db, user.email, user.password)

    if not result:
        raise HTTPException(status_code=401, detail="Erro ao logar! Email ou senha invalidos.")

    return result

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)