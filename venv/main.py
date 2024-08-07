from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

movies=[{
    "id": 1,
    "title": "Avatar",
    "overview": "En un exuberante plante...",
    "year":"2009",
    "rating": 7.8,
    "category":"Acción"
},
{
    "id": 2,
    "title": "Avatar 2",
    "overview": "En un exuberante plante...",
    "year":"2009",
    "rating": 7.8,
    "category":"Acción"
}]

class Movie(BaseModel):
    id: int
    title:str 
    overview: str
    year: int
    rating:float
    category: str

class MovieUpdate(BaseModel):
    title:str 
    overview: str
    year: int
    rating:float
    category: str


app.title="Primera aplicación con FastAPI"
app.version="2.0.0"

# < RUTAS
# - BASIC
@app.get('/', tags=['Home'])

def home():
    return "Hola Mundo!!"

# - GET
# . GET - Devolviendo Listado

@app.get('/movies', tags=['Movie'])

def get_movies() -> List[Movie]:
    return movies

# . GET - Devolviendo Uno

@app.get('/movies/{id}', tags=['Movie'])

def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie
    return []

# . GET - Devolviendo Query

@app.get('/movies/', tags=['Movie'])

def get_movie_by_category(category: str, year: int) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie
    return []

# - POST - Creando

@app.post('/movies', tags=['Movie'])

def create_movie(movie:Movie) -> List[Movie]:
    movies.append(movie.Movie.model_dump())
    return movies

# - PUT - EDITANDO

@app.put('/movies/{id}', tags=['Movie'])

def update_movie(id:int, movie:MovieUpdate) -> List[Movie]:
    for m in movies:
        if(m['id'] == id):
            m['title'] = movie.title
            m['overview'] = movie.overview
            m['year'] = movie.year
            m['rating'] = movie.rating
            m['category'] = movie.category
    return movies

# ! DELETE - Eliminar

@app.delete('/movies/{id}', tags=['Movie'])

def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies