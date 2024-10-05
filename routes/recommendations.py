from exceptions.invalid_id import IdException
from fastapi import APIRouter, Depends
from security import verify_token
from sqlalchemy.orm import Session
from fastapi import Depends
from db import MMR, SSR, UMR, USR, GMR, get_db
import json

router = APIRouter(prefix="/recommendations", dependencies=[Depends(verify_token)])

def verify_token(id: int):
  if (int(id) <= 0):
    raise IdException()

def get_recommendations(id: int, db: Session, Table: object):
  verify_token(id)
  result = db.query(Table).filter(Table.id == id).first()
  if result is None:
    return []
  recommendations = json.loads(result.recommendations)
  return [{"id": rec} for rec in recommendations]

@router.get('/movie/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    movie_recos = get_recommendations(id, db, MMR)
    return movie_recos[:5]

@router.get('/series/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    series_recos = get_recommendations(id, db, SSR)
    return series_recos[:5]

@router.get('/user/movie/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return get_recommendations(id, db, UMR)

@router.get('/user/series/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return get_recommendations(id, db, USR)

@router.get('/groups/{id}/movie', status_code=200)
async def get_group_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return get_recommendations(id, db, GMR)
