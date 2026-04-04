from config.settings import Base
from sqlalchemy import ForeignKey, Column, String, Integer, Numeric, \
    Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import Choice
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True,nullable=False)
    first_name=Column(String(30))
    last_name=Column(String(30))
    email=Column(String(50),unique=True)
    password=Column(String,nullable=False)




class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime, default=datetime.now())
    user_id=Column(Integer,ForeignKey("users.id"))

    products = relationship('Products', back_populates='category')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    desc = Column(Text, nullable=False)
    price = Column(Numeric(10, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.now())

    category = relationship('Category', back_populates='products')
    order = relationship('Orders', back_populates='products')
    user_id=Column(Integer,ForeignKey("users.id"))


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    count = Column(Integer, nullable=False, default=1)
    user_id=Column(Integer,ForeignKey("users.id"))

    products = relationship('Products', back_populates='order')