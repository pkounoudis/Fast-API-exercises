# imports
from fastapi import FastAPI

app = FastAPI()

# define endpointls
@app.get("/")
async def root():
    return {"message": "Hello World, You're rocking! This is your first FastAPI app!"}