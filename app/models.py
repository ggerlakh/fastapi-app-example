from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Zoo(Base):
    __tablename__ = "zoo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    employees = relationship("Employee", back_populates="zoo")


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    animal_type = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="animals")
    illness_dairy = relationship("IllnessDairy", back_populates="animal")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    animals = relationship("Animal", back_populates="employee")
    zoo_id = Column(Integer, ForeignKey("zoo.id"))
    zoo = relationship("Zoo", back_populates="employees")


class IllnessDairy(Base):
    __tablename__ = "illness_dairy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    animal = relationship("Animal", back_populates="illness_dairy")
    records = relationship("IllnessDairyRecord", back_populates="illness_dairy")


class IllnessDairyRecord(Base):
    __tablename__ = "illness_dairy_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(timezone=True))
    message = Column(String)
    illness_dairy_id = Column(Integer, ForeignKey("illness_dairy.id"))
    illness_dairy = relationship("IllnessDairy", back_populates="records")
