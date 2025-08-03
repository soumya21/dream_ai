# repository/my_table_repository.py
from sqlalchemy.orm import Session
from app.model.my_table import MyTable

class MyTableRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_entry(self, name: str):
        db_entry = MyTable(name=name)
        self.db.add(db_entry)
        self.db.commit()
        self.db.refresh(db_entry)
        return db_entry

    def get_entry(self, entry_id: int):
        return self.db.query(MyTable).filter(MyTable.id == entry_id).first()

    def get_entries(self, skip: int = 0, limit: int = 10):
        return self.db.query(MyTable).offset(skip).limit(limit).all()

    def delete_entry(self, entry_id: int):
        db_entry = self.db.query(MyTable).filter(MyTable.id == entry_id).first()
        if db_entry:
            self.db.delete(db_entry)
            self.db.commit()
            return True
        return False
