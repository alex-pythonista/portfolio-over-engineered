from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get('/health/')
async def health(request: Request):
    return {'message': '200 OK'}