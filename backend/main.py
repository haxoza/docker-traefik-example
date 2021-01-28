from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = [
    {"id": 1, "name": "foo"},
    {"id": 2, "name": "bar"},
    {"id": 3, "name": "foobar"},
]

@app.get("/api/")
def read_root():
    return {"status": "ok"}

@app.get("/api/items/")
def read_items():
    return items

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    try:
        item = next(item for item in items if item["id"] == item_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
