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


# Path Parameters
@app.get("/test/path-parameter/{par}")
def test_path_parameter(par):
    return {'value': par}

# path parameters with type
@app.get("/test/path-parameter-with-type/{par_int}")
def test_path_parameter_with_type(par_int: int):
    return {'value': par_int}

# order matters будет перехвачивать запросы  /test/order-matters/test

# order matters
@app.get("/test/order-matters/{path_param}")
def test_order_matters_path_param(path_param: str):
    return {'text': f'order-matters - path_param done = {path_param}'}

# order matters 2
@app.get("/test/order-matters/test")
def test_order_matters_test():
    return {"text": "order-matters - test done"}


# можно также переопределить обработку роута
# выполняться будет пепрвый get_storages

@app.get("/test/get-storages")
def get_storages():
    return [1, 2]

@app.get("/test/get-storages")
def get_storages2():
    return [3, 4]


# Когда параметр пути, являеться перечислением
from enum import Enum

# Дрпустимые параметры пути
class ModelsName(str, Enum):
    standart = 'standart'
    pro = 'pro'
    super_pro = 'super_pro'
    
@app.get("/test/models-name/{models_name}")
def models_name_rout(models_name: ModelsName):
    if models_name is ModelsName.standart:
        return ["You get standart"]
    
    if models_name is ModelsName.pro:
        return ["You get pro"]
    
    # Такой способ еще проверки есть
    if models_name.value == ModelsName.super_pro.value:
        return {"type": "super_pro", "info": "somthing"}
    
    return ["somthing wrong, models dont defined"]


# Параметр пути, которыя являеться путем
#from fastapi import Path
@app.get("/test/path-as-path/{new_path:path}")
def path_as_path(new_path):
    return [f"you send path: {new_path}"]