from sqlalchemy.orm import Session

from . import models, schemas


def get_all_zoo(db: Session):
    return db.query(models.Zoo).all()


def get_zoo(db: Session, zoo_id: int):
    return db.query(models.Zoo).filter(models.Zoo.id == zoo_id).first()


def get_zoo_by_name(db: Session, name: str):
    return db.query(models.Zoo).filter(models.Zoo.name == name).first()


def create_zoo(db: Session, zoo: schemas.ZooCreate):
    db_zoo = models.Zoo(**zoo.model_dump())
    db.add(db_zoo)
    db.commit()
    db.refresh(db_zoo)
    return db_zoo


def delete_zoo(db: Session, zoo_id: int):
    deleted_zoo = get_zoo(db, zoo_id)
    db.query(models.Zoo).filter(models.Zoo.id == zoo_id).delete()
    db.commit()
    return deleted_zoo


def get_all_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Zoo).filter(models.Employee.id == employee_id).first()


def create_employee(db: Session, employee: schemas.EmployeeCreate, zoo_id: int):
    db_employee = models.Employee(**employee.model_dump(), zoo_id=zoo_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    deleted_employee = get_employee(db, employee_id)
    db.query(models.Employee).filter(models.Employee.id == employee_id).delete()
    db.commit()
    return deleted_employee


def get_all_animals(db: Session):
    return db.query(models.Animal).all()


def get_animal(db: Session, animal_id: int):
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()


def create_animal(db: Session, animal: schemas.AnimalCreate, employee_id: int):
    db_animal = models.Animal(**animal.model_dump(), employee_id=employee_id)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


def delete_animal(db: Session, animal_id: int):
    deleted_animal = get_animal(db, animal_id)
    db.query(models.Animal).filter(models.Animal.id == animal_id).delete()
    db.commit()
    return deleted_animal


def get_all_illness_dairys(db: Session):
    return db.query(models.IllnessDairy).all()


def get_illness_dairy(db: Session, illness_dairy_id: int):
    return db.query(models.IllnessDairy).filter(models.IllnessDairy.id == illness_dairy_id).first()


def create_illness_dairy(db: Session, illness_dairy_create: schemas.IllnessDairyCreate, animal_id: int):
    db_illness_dairy = models.IllnessDairy(**illness_dairy_create.model_dump(), animal_id=animal_id)
    db.add(db_illness_dairy)
    db.commit()
    db.refresh(db_illness_dairy)
    return db_illness_dairy


def delete_illness_dairy(db: Session, illness_dairy_id: int):
    deleted_illness_dairy = get_illness_dairy(db, illness_dairy_id)
    db.query(models.IllnessDairy).filter(models.IllnessDairy.id == illness_dairy_id).delete()
    db.commit()
    return deleted_illness_dairy


def get_all_illness_dairy_records(db: Session, illness_dairy_id: int):
    return db.query(models.IllnessDairyRecord).filter(models.IllnessDairyRecord.illness_dairy_id == illness_dairy_id).all()


def get_illness_dairy_record(db: Session, illness_dairy_record_id: int):
    return db.query(models.IllnessDairyRecord).filter(models.IllnessDairyRecord.id == illness_dairy_record_id).first()


def create_illness_dairy_record(db: Session, illness_dairy_record: schemas.IllnessDairyRecordCreate, illness_dairy_id: int):
    db_illness_dairy_record = models.IllnessDairyRecord(**illness_dairy_record.model_dump(), illness_dairy_id=illness_dairy_id)
    db.add(db_illness_dairy_record)
    db.commit()
    db.refresh(db_illness_dairy_record)
    return db_illness_dairy_record


def delete_illness_dairy_record(db: Session, illness_dairy_record_id: int):
    deleted_illness_dairy_record = get_illness_dairy_record(db, illness_dairy_record_id)
    db.query(models.IllnessDairyRecord).filter(models.IllnessDairyRecord.id == illness_dairy_record_id).delete()
    db.commit()
    return deleted_illness_dairy_record