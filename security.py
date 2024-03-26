from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
SECRET = os.getenv('SECRET')

print(SECRET)

def require_secret(view_func):
    @wraps(view_func)
    def decorated_function(*args, **kwargs):
      secret = request.headers.get('Secret')
      if secret != SECRET:
        return jsonify({
            "error": "Invalid secret",
            "statusCode": 401,
            "description": "Unauthorized"
        }), 401
      return view_func(*args, **kwargs)
    return decorated_function
