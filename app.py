from fastapi import APIRouter, FastAPI, Depends
import uvicorn
from security import SecretException, invalid_secret_exception_handler, verify_token
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from db import MMR, get_db

app = FastAPI()
authenticated = APIRouter(dependencies=[Depends(verify_token)])

@authenticated.get('/health', status_code=200)
async def home():
  return "Alive"

@authenticated.get('/recommendations/movie/{id}', status_code=200)
async def get_movie_recommendation(id:int, db: Session = Depends(get_db)):
    result = db.query(MMR).filter(MMR.id == id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result.recommendations

# Esta linea debe estar después de todos los métodos:
app.include_router(authenticated)
app.add_exception_handler(SecretException, invalid_secret_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app)
