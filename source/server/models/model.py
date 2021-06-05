from sqlalchemy import Table, Float, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dataclasses import dataclass

"""Firstly we need a mapping in order to show sqlalchemy how the database seems out"""
Base= declarative_base() # is used for mapping
 # this makes the connection to the database
# declarative_base() returns the base class used for table descriptions

# Create Class describing the cars table. Inherits from Base from above.
@dataclass
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    rentStartDate = Column(String)
    rentEndDate = Column(String)
    price = Column(Float)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates='cars')

    # Create Class describing the customers table. Inherits from Base from above.
@dataclass
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    address = Column(String)
    phone_number = Column(Integer)
    city = Column(String)
    cars = relationship("Car", back_populates="customer")

