from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Databse ulanish
SQLALCHEMY_DATABASE_URL = "postgresql://user@localhost:5432/fastapi"
# 2. Engine yaratish (bazaga kirish )
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. SessionLocal (har bir so'rov uchun alohida sessiya)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Asosiy klass (model tuzish uchun)
Base = declarative_base()