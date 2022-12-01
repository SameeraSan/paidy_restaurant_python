from sqlalchemy import  Column, Integer, String
from config import Base


class Items(Base):
    __tablename__ ="Items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Integer)
    price = Column(Integer)


class Order(Base):
    __tablename__ ="Order"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    table_id = Column(Integer)
    item_id = Column(Integer)
    status = Column(Integer)
    cook_time = Column(Integer)
    quantity = Column(Integer)
    notes = Column(String)

class Tables(Base):
    __tablename__ ="Tables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    capacity = Column(Integer)
    status = Column(Integer)
    