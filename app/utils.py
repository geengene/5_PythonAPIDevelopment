from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

def hash(password: str):
  return  pwd_context.hash(password) # hash the password of user.password)
