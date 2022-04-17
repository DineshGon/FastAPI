from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

##D1S
##.DB Connection using sqlalchemy

# creating the path
SQLALCHEMY_DATABASE_URL = "sqlite:///./appointments1.db"

# creating the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# creating the session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# creating the base
Base = declarative_base()


##D1E

def get_db():
    db = SessionLocal()  # its from the database
    try:
        yield db
    finally:
        db.close()  # if everything is done close the db
