from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get('/')
def root():
    return {"hello": "world"}

@app.post('/items')
def create_item(item: Item):
    items.append(item)
    return items

@app.get('/items', response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail='Item not found')
