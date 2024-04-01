from exceptions.invalid_id import IdException, invalid_id_exception_handler
from exceptions.invalid_secret import SecretException, invalid_secret_exception_handler
from fastapi import APIRouter, FastAPI, Depends
import uvicorn
from security import verify_token
from fastapi import Depends
from routes import recommendations

app = FastAPI()
authenticated = APIRouter(dependencies=[Depends(verify_token)])

@authenticated.get('/health', status_code=200)
async def home():
  return "Alive"

# Estas lineas deben estar después de todos los métodos:
app.include_router(authenticated)
app.include_router(recommendations.router)
app.add_exception_handler(SecretException, invalid_secret_exception_handler)
app.add_exception_handler(IdException, invalid_id_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app)
