from app.channels.response import response, send, error
from app.channels.endpoints import WebSocketEndpoint
from typing import Dict
import logging
import json
import sys


def dispatch(ws, raw_data: str):
    try:
        data = json.loads(raw_data)
        if data['mode'] == 'request':
            router(ws, data['endpoint'], data['data'])
            return
        send(ws, response(sys._getframe().f_code.co_name, {'message': 'OK!'}))
    except Exception as err:
        logging.error(str(err), exc_info=True)
        send(ws, error(sys._getframe().f_code.co_name, str(err)))
        return


def router(ws, endpoint: str, data: Dict):
    endpoints = WebSocketEndpoint()
    if hasattr(endpoints, endpoint):
        action = getattr(endpoints, endpoint)
        action(ws, data)
        return
    send(ws, response(sys._getframe().f_code.co_name, {'message': 'OK!'}))
