from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Object):
   __tablename__ = 'Product'
   id = Column(String, primary_key=True)
   price = Column(Float)
   picturelink = Column(String)
   description = Column(String)
