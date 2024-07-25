from typing import Dict
import json


RES_STATUS = {
    'PENDING': 0,
    'SUCCESS': 1,
}


def response(endpoint: str, status: int, data: Dict) -> Dict:
    return {
        'mode': 'response',
        'endpoint': endpoint,
        'status': status,
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
