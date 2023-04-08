from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import URL, create_engine

url = URL.create(
    drivername="sqlite",
    database="pass.db"
)

Base = declarative_base()
engine = create_engine(url)
session = sessionmaker(bind=engine)()



