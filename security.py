from typing import Annotated
from fastapi import Header, Request
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse

load_dotenv()
SECRET = os.getenv('SECRET')

class SecretException(Exception):
  pass

async def invalid_secret_exception_handler(request: Request, exc: SecretException):
  return JSONResponse(
    status_code=401,
    content={
        "error": "Invalid secret",
        "statusCode": 401,
        "description": "Unauthorized"
      },
  )

async def verify_token(Secret: Annotated[str, Header()]):
  print("AFUERAAA")
  print(Secret)
  print(SECRET)
  if Secret != SECRET:
    print("ENTREEEE")
    raise SecretException()

""" def require_secret(func):
  def decorated_function(*args, **kwargs):
    secret = request.headers.get('Secret')
    print("Holaaaa")
    if "secret" != SECRET:
      return {
        "error": "Invalid secret",
        "statusCode": 401,
        "description": "Unauthorized"
      }, 401
    return func(*args, **kwargs)
  return decorated_function """
