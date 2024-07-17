from app.libraries.obsws.client import OBSClient
from typing import Dict, List


client = OBSClient()


def get_obs_version() -> Dict:
    return client.get_version()


def get_scene_item_list(scene_name: str) -> List:
    data = []
    res = client.get_scene_item_list(scene_name)
    for r in res:
        data.append({
            'sceneId': r['sceneItemId'],
            'sourceName': r['sourceName'],
            'isEnabled': r['sceneItemEnabled'],
        })
    return data


def find_item_id_by_source_name(scene_name: str, source_name: str) -> (int | None):
    res = get_scene_item_list(scene_name)
    for i in res:
        if source_name == i['sourceName']:
            return i['sceneId']
    return None


def get_item_enabled(scene_name: str, item_id: int) -> bool:
    return client.get_scene_item_enabled(scene_name, item_id)


def toggle_item_enabled(scene_name: str, item_id: int):
    if get_item_enabled(scene_name, item_id):
        client.set_scene_item_enabled(scene_name, item_id, False)
    else:
        client.set_scene_item_enabled(scene_name, item_id, True)


def set_item_enabled(scene_name: str, item_id: int):
    client.set_scene_item_enabled(scene_name, item_id, True)


def set_item_disabled(scene_name: str, item_id: int):
    client.set_scene_item_enabled(scene_name, item_id, False)
