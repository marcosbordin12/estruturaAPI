from sqlalchemy.orm import Session
from app.models import User

def create_user(db: Session, name, email, password):
    user = User(name=name, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email):
    return db.query(User).filter(User.email == email).first()

def list_users(db: Session):
    return db.query(User).all()