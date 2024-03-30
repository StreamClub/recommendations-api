import json
from db import InvalidIdError, MovieDb
from flask import Flask, jsonify
from security import require_secret

app = Flask(__name__)
db = MovieDb()

@app.route("/recommendations/movie/<id>")
@require_secret
def get_movie_recommendation(id):
  print(id)
  try:
    recs = json.loads(db.get_movie_movie_recommendation(id))
  except InvalidIdError as e:
    print(str(e))
    return jsonify({'error': 'Invalid ID: ID must be a positive integer.'}), 400
  return [{"id": rec} for rec in recs]

""" if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("5000"))  """