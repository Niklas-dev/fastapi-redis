from ...db.database import Base
from sqlalchemy import Column, Integer, String


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, default="Test data")
