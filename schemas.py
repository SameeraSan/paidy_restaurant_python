from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class TableSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    capacity: Optional[int] = None
    status: Optional[int] = None


class ItemSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[int] = None
    status: Optional[int] = None   

class OrderSchema(BaseModel):
    id: Optional[int] = None
    order_id: Optional[str] = None
    table_id: Optional[int] = None
    item_id: Optional[int] = None  
    status: Optional[int] = None  
    cook_time: Optional[int] = None  
    quantity: Optional[int] = None  
    notes: Optional[str] = None  

class Config:
    orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)

class RequestTable(BaseModel):
    parameter: TableSchema = Field(...)

class RequestOrder(BaseModel):
    parameter: OrderSchema = Field(...)        