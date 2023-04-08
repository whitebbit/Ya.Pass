import datetime
from sqlalchemy.sql import sqltypes as types
from sqlalchemy import Column
from sqlalchemy_utils import database_exists

import database


def initialize():
    if database_exists(database.url):
        return
    database.Base.metadata.create_all(database.engine)


class Pass(database.Base):
    __tablename__ = "pass"

    id = Column(types.Integer, primary_key=True)
    service = Column(types.String)
    token = Column(types.BINARY)
    updated = Column(types.Date, default=datetime.datetime.now())

    def __repr__(self):
        return f"{self.id} | {self.service} | {self.updated}"


initialize()
