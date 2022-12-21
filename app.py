from datetime import date, datetime
from typing import Optional

from pythagoras import Pythagoras
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, bday: Optional[str] = None):
    if bday is None:
        return templates.TemplateResponse("home.html", {"request": request})
    dte = datetime.strptime(bday, '%Y-%m-%d').date()
    pythagoras = Pythagoras(dte.day, dte.month, dte.year)
    context = {
        "request": request,
        'nums': pythagoras.nums,
        'variables': pythagoras.variables,
        'info': 'Pythagoras Matrix',
    }
    return templates.TemplateResponse("index.html", context)


# @app.get('/')
# def home(day: str, month: str, year: str):
#     pythagoras = Pythagoras(day, month, year)
#     return {'nums': pythagoras.nums, 'variables': pythagoras.variables}
