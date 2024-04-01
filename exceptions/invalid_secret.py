from fastapi import Request
from fastapi.responses import JSONResponse

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