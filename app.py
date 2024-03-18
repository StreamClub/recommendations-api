from db import MovieDb
from flask import Flask

app = Flask(__name__)
db = MovieDb()

@app.route("/recommendations/movie/<id>")
def get_movie_recommendation(id):
  return db.get_movie_movie_recommendation(id)