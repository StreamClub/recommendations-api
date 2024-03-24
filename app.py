import json
from db import MovieDb
from flask import Flask

app = Flask(__name__)
db = MovieDb()

@app.route("/recommendations/movie/<id>")
def get_movie_recommendation(id):
  recs = json.loads(db.get_movie_movie_recommendation(id))
  return [{"id": rec} for rec in recs]

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("5000")) 