from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    order_date = Column(DateTime)
    status = Column(String)

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    order_date: DateTime
    status: str

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: DateTime
    status: str

    class Config:
        orm_mode = True
