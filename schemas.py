from typing import List

from pydantic import BaseModel
from datetime import date


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    # genres: str = None # используем для необязательного ввода данных
    genres: List[Genre]
    pages: int
