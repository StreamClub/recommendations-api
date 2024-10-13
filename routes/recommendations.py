from asyncio import sleep
from exceptions.invalid_id import IdException
from fastapi import APIRouter, Depends, HTTPException
from security import verify_token
from sqlalchemy.orm import Session
from fastapi import Depends
from db import MMR, SSR, UMR, USR, GMR, get_db
import json

router = APIRouter(prefix="/recommendations", dependencies=[Depends(verify_token)])

def retry_on_exception(func):
  async def wrapper(*args, **kwargs):
      max_retries = 5
      retry_delay = 1
      for _ in range(max_retries):
         try:
            
            return await func(*args, **kwargs)
         except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Retrying in {retry_delay} seconds")
            await sleep(retry_delay)
      raise HTTPException(status_code=500, detail="Could not retrieve recommendations")
  return wrapper

def verify_token(id: int):
  if (int(id) <= 0):
    raise IdException()

@retry_on_exception
async def get_recommendations(id: int, db: Session, Table: object):
  verify_token(id)
  result = db.query(Table).filter(Table.id == id).first()
  if result is None:
    return []
  recommendations = json.loads(result.recommendations)
  return [{"id": rec} for rec in recommendations]

@router.get('/movie/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    movie_recos = await get_recommendations(id, db, MMR)
    return movie_recos[:5]

@router.get('/series/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    series_recos = await get_recommendations(id, db, SSR)
    return series_recos[:5]

@router.get('/user/movie/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return await get_recommendations(id, db, UMR)

@router.get('/user/series/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return await get_recommendations(id, db, USR)

@router.get('/groups/{id}/movie', status_code=200)
async def get_group_movie_recommendation(id:int, db: Session = Depends(get_db)):
    return await get_recommendations(id, db, GMR)
