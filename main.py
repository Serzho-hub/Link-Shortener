from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import secrets
import string
from database import init_db, save_url, get_original_url

app = FastAPI(title="URL Shortener", description="Сервис укорачивания ссылок", version="0.2.0")

init_db()

class URLRequest(BaseModel):
    url: str

def generate_short_code(length: int = 6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

@app.post("/shorten")
def shorten_url(request: URLRequest):
    original_url = request.url
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url
    short_code = generate_short_code()
    save_url(short_code, original_url)
    return {"short_code": short_code, "short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
def redirect_to_original(short_code: str):
    original_url = get_original_url(short_code)
    if original_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=original_url)