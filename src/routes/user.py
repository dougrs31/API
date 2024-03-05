from fastapi import APIRouter, Response, status
from ..config.db import conn
from ..models.user import users
from ..schemas.user import Data
from starlette.status import HTTP_204_NO_CONTENT

data = APIRouter()

@data.get('/opiniones', response_model=list[Data], tags=["opiniones"])
def get_opiniones():
    return conn.execute(users.select()).fetchall()

@data.post('/opiniones', response_model=Data, tags=["opiniones"])
def create_opinion(opinion: Data):
    new_opinion = {"calname": opinion.calname, 
                   "username": opinion.username, 
                   "comentario": opinion.comentario, 
                   "calificacion": opinion.calificacion}
    conn.execute(users.insert().values(new_opinion))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@data.get('/opiniones/{id}', response_model=Data, tags=["opiniones"])
def get_opinion(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@data.delete('/opiniones/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["opiniones"])
def delete_opinion(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@data.put('/opiniones/{id}', response_model=Data, tags=["opiniones"])
def update_opinion(id: str, opinion: Data):
    conn.execute(users.update().values(
        calname = opinion.calname, 
        username = opinion.username, 
        comentario = opinion.comentario, 
        calificacion = opinion.calificacion).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

