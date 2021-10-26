from typing import List

from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author

app = FastAPI()


#
# @app.get('/')
# def home():
#     return {"key": "Hello"}

#
# @app.get('/{pk}')
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}

#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}

# quantity: int = Body(...) 'quantity' мы добавили в тело запроса, иначе он был бы запросом
@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"item": item, 'author': author, 'quantity': quantity}


# создаем автора по модели
@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}


# задаем параметры для запроса (валидацию)
# def get_book(q: str = Query(None)):
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


# Получаем книгу по id
# Path() добаление дополнительных параметров
# gt=1, le=20 ограничение значения параметра, т.е. параметр должен быть в пределе 2-20
# pages дополнительный параметр с ограничение значения параметра
@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=2, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}
