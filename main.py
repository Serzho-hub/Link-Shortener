from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Serzho Shortener API is alive!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}