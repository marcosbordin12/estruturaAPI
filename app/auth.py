from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "123@!#"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)

def create_token(email):
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)