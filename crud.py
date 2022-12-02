from sqlalchemy.orm import Session
from models import Items, Order, Tables
from schemas import ItemSchema, OrderSchema, TableSchema
import random


def get_table_items(db: Session, table_id: int):
    return db.query(Order).filter(Order.table_id == table_id).all()

def get_order_by_table_item(db: Session, table_id: int, item_id: int):
    return db.query(Order).filter(Order.table_id == table_id,Order.item_id == item_id).first()

def create_order(db: Session, order: OrderSchema):
    _order = Order(order_id=order.order_id, table_id=order.table_id, item_id=order.item_id, status=order.status, cook_time=order.cook_time, quantity=order.quantity, notes=order.notes)
    _order.cook_time = random.randint(5,15)
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order    

def remove_order(db: Session, table_id: int, item_id: int):
    _order = get_order_by_table_item(db=db, table_id=table_id, item_id=item_id)
    db.delete(_order)
    db.commit()
