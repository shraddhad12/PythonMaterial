from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)



engine = create_engine('C:///Users/Shraddha/Downloads/sqlite-dll-win-x64-3450300/sqlite3.dll"')
Base.metadata.create_all(engine)