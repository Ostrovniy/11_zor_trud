from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offert: bool | None = None
    

@app.get("/")
async def root():
    return {"text": "hello"}

# Первый запрос: GET /users
# Комментрий 1
@app.get("/users")
def read_users():
    return [
        {'name': 'vasia1', 'phone': '777'}, 
        {'name': 'vasia2', 'phone': '888'}
    ]

# Второй запрос: POST /posts
# Комментрий 2
@app.get("/posts")
def read_posts():
    # Теперь этот эндпоинт принимает данные (через data) и возвращает список
    return [
        {'title': 'заголовок1', 'content': 'контент1'}, 
        {'title': 'заголовок2', 'content': 'контент2'}
    ]
    
@app.put('/items/{item_id}')
def test_put(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}