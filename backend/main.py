from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    item: int


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/copy-miro-board")
def copy_miro_board(item: Item):
    print("test")
    return {"item": item.item}

# @app.put("/copy-miro-board")
# def copy_miro_board(item_id: int, q: str):
#     print("test")
#     return {"item_id": item_id, "q": q}
