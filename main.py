from typing import Union


from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()


class Item(BaseModel):
    name:str
    price:float
    is_offer:Union[bool,None]=None


@app.get('/')
def read_root():
    """
        it return dictionary to be converted to a JSON format

    """
    return {
        'hello':'World'
    }

@app.get("/items/{item_id}")
# get item_id as var to pass in param
def read_item(item_id: int, q: Union[str, None] = None):
    """
        item_id must be a int
        q:accepts both  strings and None
    """
    
    return {"item_id": item_id, "q": q}


@app.get('/test_items/{item_id}')
def put_item(item_id:int,item:Item):
    return {
        'item_id':item_id,
        'item_name':item.name,
        'item_price':item.price,
    }