from app.channels.response import response, send
import json


def dispatch(ws, raw_data: str):
    data = json.loads(raw_data)
    if data['mode'] == 'request':
        router(ws, data['endpoint'])
    send(ws, response('index', {'ping': 'OK!'}))


def router(ws, endpoint: str):
    pass
