import jwt
from datetime import datetime, timedelta

SECRET_KEY = "pao"
ALGORITHM = "HS256"

def crear_token(data: dict, expira_en_min=30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expira_en_min)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        return None
    except jwt.InvalidTokenError:
        print("Token inválido")
        return None
