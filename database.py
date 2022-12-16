from sqlalchemy import create_engine

# where our database will be and type of daatbase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# initialise our database


# create sqlite url
SQLALCHEMY_URL = "sqlite:///todo.db"

# create new engine instance
engine = create_engine(SQLALCHEMY_URL)

# Create session for  accessing databse
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Create declaritive base meta instance
Base = declarative_base()
