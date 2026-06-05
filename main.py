from fastapi import FastAPI

app = FastAPI(title="URL Shortener", description="Простой сервис для укорачивания ссылок", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Serzho Shortener API is alive!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}