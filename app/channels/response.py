from typing import Dict
import json


def response(endpoint: str, data: Dict) -> Dict:
    return {
        'mode': 'response',
        'endpoint': endpoint,
        'data': data,
    }


def error(endpoint: str, msg: str) -> Dict:
    return {
        'mode': 'error',
        'endpoint': endpoint,
        'data': {
            'message': msg,
        },
    }


def to_json(data: Dict) -> str:
    return json.dumps(data, ensure_ascii=True)


def send(ws, data: Dict):
    ws.send(to_json(data))
