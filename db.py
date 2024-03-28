from dotenv import load_dotenv
import psycopg2
import os

class InvalidIdError(Exception):
  pass

class MovieDb:
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
    self.conn.close()  