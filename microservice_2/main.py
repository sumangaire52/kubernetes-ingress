from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "You requested microservice 2"}
