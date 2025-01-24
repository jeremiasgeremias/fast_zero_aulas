from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_zero.schema import Message

app = FastAPI()


@app.get('/', status_code = HTTPStatus.OK, response_model = Message)
def read_root():
    return {'message': 'Olá Mundo!'}
