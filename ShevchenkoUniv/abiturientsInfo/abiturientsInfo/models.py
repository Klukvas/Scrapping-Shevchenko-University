from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Float

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"),  pool_pre_ping=True)

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class AbiturientRow(DeclarativeBase):
    __tablename__ = 'abiturients'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100))
    mark = Column(Float())
    priority = Column(String(100))
    status = Column(String(100))
    docs = Column(String(100))
    faculty = Column(String(100))
    specialty = Column(String(100))
