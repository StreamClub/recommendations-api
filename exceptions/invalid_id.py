from fastapi.responses import JSONResponse
from fastapi import Request

class IdException(Exception):
  pass

async def invalid_id_exception_handler(request: Request, exc: IdException):
  return JSONResponse(
    status_code=400,
    content={
        "error": "Invalid id: must be a positive number",
        "statusCode": 400,
        "description": "Bad Request"
      },
  )