from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal() # makes a session towards the database for every request to that API endpoint, and closes when done.
    try:
        yield db
    finally:
        db.close()

# while True:
#   try:
#     conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0490258', cursor_factory=RealDictCursor)
#     cur = conn.cursor()
#     print("Connection to database successful")
#     break
#   except Exception as error:
#     print("Connection failed\nError:", error)
#     time.sleep(2)