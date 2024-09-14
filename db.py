import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

class InvalidIdError(Exception):
  pass

engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define una función para obtener la sesión de base de datos
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

class MMR(Base):
  __tablename__ = "movie_movie_recommendation"

  id = Column(Integer,primary_key=True,nullable=False)
  recommendations = Column(String,nullable=False)

  def __str__(self):
    return f"Recommendations for movie with id {self.id}: {self.recommendations}"

class SSR(Base):
  __tablename__ = "series_series_recommendation"

  id = Column(Integer,primary_key=True,nullable=False)
  recommendations = Column(String,nullable=False)

  def __str__(self):
    return f"Recommendations for series with id {self.id}: {self.recommendations}"
  
class UMR(Base):
  __tablename__ = "user_movie_recommendation"

  id = Column(Integer,primary_key=True,nullable=False)
  recommendations = Column(String,nullable=False)

  def __str__(self):
    return f"Movie recommendations for user with id {self.id}: {self.recommendations}"

class USR(Base):
  __tablename__ = "user_series_recommendation"

  id = Column(Integer,primary_key=True,nullable=False)
  recommendations = Column(String,nullable=False)

  def __str__(self):
    return f"Series recommendations for user with id {self.id}: {self.recommendations}"