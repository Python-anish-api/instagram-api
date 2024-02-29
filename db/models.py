from .database import Base
from sqlalchemy import Column, String, Integer 


class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)