from app.repository import create_user, get_user_by_email, list_users
from app.auth import hash_password, verify_password, create_token

def register_user(db, name, email, password):
    hashed = hash_password(password)
    return create_user(db, name, email, hashed)

def login_user(db, email, password):
    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_token(user.email)

    return {"access_token": token}

def get_users(db):
    return list_users(db)