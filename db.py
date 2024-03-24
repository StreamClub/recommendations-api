from dotenv import load_dotenv
import psycopg2
import os

class MovieDb:
  def __init__(self):
    print("Init")
    load_dotenv()
    connection_string = os.getenv('DATABASE_URL')
    print(connection_string)
    conn = psycopg2.connect(connection_string)
    print("Connected")
    self.cur = conn.cursor()
    self.conn = conn
    print("Cursor")

  def get_movie_movie_recommendation(self, id):
    query = f"SELECT recommendations FROM movie_movie_recommendation WHERE Id = {id}" #TO DO: fix sql injection
    self.cur.execute(query)
    if (self.cur.rowcount == 0):
      return "[]"
    print(self.cur.rowcount)
    return self.cur.fetchone()[0]
  
  def __del__(self):
    self.cur.close()
    self.conn.close()  
    print("Cierro todo")