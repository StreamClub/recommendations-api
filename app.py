from fastapi import FastAPI
import uvicorn
import asyncio
import sys
# from security import require_secret
from db import InvalidIdError, MovieDb
from sqlalchemy.orm import Session

from fastapi import HTTPException, Depends
from starlette import status

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv('DATABASE_URL')

engine = create_engine(connection_string)

Base = declarative_base()

class MMR(Base):
    __tablename__ = "movie_movie_recommendation"

    id = Column(Integer,primary_key=True,nullable=False)
    recommendations = Column(String,nullable=False)

    def __str__(self):
        return f"Recommendations for movie with id {self.id}: {self.recommendations}"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

app = FastAPI()

@app.get('/')
async def home():
  return "Hello from rootxcs"

@app.get('/recommendations/movie/{id}')
# @require_secret
async def get_movie_recommendation(id:int):
  
  result = session.query(MMR).filter(MMR.id == id).first()
  if result is None:
    raise HTTPException(status_code=404, detail="Item not foundd")
  return result.recommendations

if __name__ == "__main__":
    uvicorn.run(app)