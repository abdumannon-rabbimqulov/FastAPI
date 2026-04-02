from config.settings import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True,nullable=False)
    first_name=Column(String(30))
    last_name=Column(String(30))
    email=Column(String(50),unique=True)