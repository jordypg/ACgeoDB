#connect to db
from sqlalchemy import create_engine, Column, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:geodb@localhost/project'

engine = create_engine(DATABASE_URL)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


