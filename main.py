from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book')
def create_book(item: Book):
    return item

@app.get('/book')
def get_book(q: str = Query(None, min_length=2, max_length=5, description="Search book")):  # задаем параметры для запроса (валидацию)
                                                                                            # description описание поля в документции
    return q

