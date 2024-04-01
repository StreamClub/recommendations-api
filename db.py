from dotenv import load_dotenv
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

""" class MovieDb:
  def __init__(self):
    load_dotenv()
    connection_string = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(connection_string)
    self.cur = conn.cursor()
    self.conn = conn

  def get_movie_movie_recommendation(self, id):
    if (not id.isnumeric()) or int(id) <= 0:
      print(f"Error with {id}")
      raise InvalidIdError("Invalid Movie ID")
    query = "SELECT recommendations FROM movie_movie_recommendation WHERE Id = %s"
    self.cur.execute(query, (id,))
    if self.cur.rowcount == 0:
      return "[]"
    return self.cur.fetchone()[0]
  
  def __del__(self):
    self.cur.close()
    self.conn.close()  """ 