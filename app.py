# Pruebas con FastAPI y enviroments

# https://jovian.com/biraj/deploying-a-machine-learning-model
# ejecutar usando uvicorn app:app --reload

from fastapi import FastAPI
# import nest_asyncio
import uvicorn
import sys
import pickle
import sklearn

# cv = pickle.load(open('models/smokers.pk1' , 'rb'))

app = FastAPI()
@app.get('/index')
async def home():
  return "Hello from index"

@app.get('/')
async def home():
  return "Hello from root"

# @app.get('/predict/{text}')
# async def predict(text: str):
#   text = [text]
#   vect = cv.transform(text).toarray()
#   my_prediction = clf.predict(vect)
#   return my_prediction[0]

@app.get('/{name}')
async def home(name: str):
  return "Hello " + name + ". How are you doing today?"


# enviar query params
# los query params siempre deben tener un valor por defecto
# los query params opcionales siempre deben tener "or None"
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str or None = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# @app.get("/modules/versions")
# async def get_version():
#     return {pickle: pickle.format_version, sklearn: sklearn.__version__}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

