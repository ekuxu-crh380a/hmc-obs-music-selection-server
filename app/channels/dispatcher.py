from app.channels.response import response, send
from app.channels.endpoints import WebSocketEndpoint
from typing import Dict
import json


def dispatch(ws, raw_data: str):
    data = json.loads(raw_data)
    if data['mode'] == 'request':
        router(ws, data['endpoint'], data['data'])
        return
    send(ws, response('index', {'message': 'OK!'}))


def router(ws, endpoint: str, data: Dict):
    endpoints = WebSocketEndpoint()
    action = getattr(endpoints, endpoint)
    action(ws, data)
