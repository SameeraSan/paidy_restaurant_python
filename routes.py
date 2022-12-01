from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, ItemSchema, OrderSchema, TableSchema, RequestOrder

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/item/{table_id}")
async def get_items(table_id : int, db: Session = Depends(get_db)):
    _items = crud.get_table_items(db, table_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)

@router.get("/item/{table_id}/{item_id}")
async def get_order_by_table_item(table_id : int, item_id : int, db: Session = Depends(get_db)):
    _items = crud.get_order_by_table_item(db, table_id, item_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)


@router.post("/order")
async def create_order_service(request: OrderSchema, db: Session = Depends(get_db)):
    crud.create_order(db, request)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)

@router.delete("/delete/{table_id}/{item_id}")
async def remove_order(table_id: int, item_id: int, db: Session = Depends(get_db)):
    crud.remove_order(db, table_id=table_id, item_id=item_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

