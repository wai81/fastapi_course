from typing import List

from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}

#
# @app.get('/{pk}')
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book')
def create_book(item: Book):
    return item


# задаем параметры для запроса (валидацию)
#
# '...' указываем что наш параметр 'q' обязательный
#
# 'description' описание параметра 'q' в документции
#
# 'regex=' параметры по регуларного выражения
# def get_book(q: str = Query(..., description="Search book", regex="test")):
#
# устанавливаем параметр "test" по умолчанию
# def get_book(q: str = Query("test", description="Search book")):
#
# передача списка параметров List[] и добавляем в список значения пол умолчанию ["test1", "test2"]
# def get_book(q: List[str] = Query(["test1", "test2"], description="Search book", deprecated=True)):
# deprecated=True это означает что данный параметр устаревший и будет удален
@app.get('/book')
def get_book(q: List[str] = Query(["test1", "test2"], description="Search book", deprecated=True)):
    return q
