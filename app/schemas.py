from pydantic import BaseModel, EmailStr
from datetime import datetime


class IllnessDairyRecordBase(BaseModel):
    date: datetime
    message: str


class IllnessDairyRecordCreate(IllnessDairyRecordBase):
    pass


class IllnessDairyRecord(IllnessDairyRecordBase):
    id: int
    illness_dairy_id: int

    class Config:
        orm_mode = True


class IllnessDairyBase(BaseModel):
    pass


class IllnessDairyCreate(IllnessDairyBase):
    pass


class IllnessDairy(IllnessDairyBase):
    id: int
    animal_id: int
    records: list[IllnessDairyRecord]

    class Config:
        orm_mode = True


class AnimalBase(BaseModel):
    name: str
    animal_type: str


class AnimalCreate(AnimalBase):
    pass


class Animal(AnimalBase):
    id: int
    employee_id: int
    illness_dairy: IllnessDairy

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    name: str
    surname: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    animals: list[Animal]
    zoo_id: int
    
    class Config:
        orm_mode = True


class ZooBase(BaseModel):
    name: str


class ZooCreate(ZooBase):
    pass


class Zoo(ZooBase):
    id: int
    employees: list[Employee]

    class Config:
        orm_mode = True