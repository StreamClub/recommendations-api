from typing import Annotated
from exceptions.invalid_secret import SecretException
from fastapi import Header
from dotenv import load_dotenv
import os

load_dotenv()
SECRET = os.getenv('SECRET')

async def verify_token(Secret: Annotated[str, Header()]):
  if Secret != SECRET:
    raise SecretException()
