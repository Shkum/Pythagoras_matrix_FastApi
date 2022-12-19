from fastapi import FastAPI
from pythagoras import Pythagoras

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'test'}


@app.get('/date')
def home(day: str, month: str, year: str):
    pythagoras = Pythagoras(day, month, year)
    return {'nums': pythagoras.nums, 'variables': pythagoras.variables}
