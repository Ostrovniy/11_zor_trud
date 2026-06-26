from fastapi import FastAPI

app = FastAPI()

# Первый запрос: GET /users
@app.get("/users")
def read_users():
    return [
        {'name': 'vasia1', 'phone': '777'}, 
        {'name': 'vasia2', 'phone': '888'}
    ]

# Второй запрос: POST /posts
@app.get("/posts")
def read_posts():
    # Теперь этот эндпоинт принимает данные (через data) и возвращает список
    return [
        {'title': 'заголовок1', 'content': 'контент1'}, 
        {'title': 'заголовок2', 'content': 'контент2'}
    ]