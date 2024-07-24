from app.settings import DATA_DIR
from typing import List, Dict
import json

TARGET_LEVEL = ['12', '12+', '13', '13+', '14']


def build_music_row(music: Dict) -> Dict:
    return {
        'id': music['id'],
        'title': music['basic_info']['title'],
        'artist': music['basic_info']['artist'],
        'type': music['type'],
        'level': music['tmp_level'],
        'difficulty': music['tmp_difficulty'],
    }


def musiclist() -> List:
    with open(f"{DATA_DIR}/music_data.json", 'r', encoding='utf-8') as file:
        raw_data = json.load(file)
    music_data = []
    for music in raw_data:
        for (idx, level) in enumerate(music['level']):
            for target in TARGET_LEVEL:
                if level == target and idx >= 2:
                    music['tmp_level'] = level
                    music['tmp_difficulty'] = idx
                    music_data.append(build_music_row(music))
    return music_data


def id2music(id, difficulty) -> Dict:
    music_data = musiclist()
    for music in music_data:
        if id == music["id"] and difficulty == music['difficulty']:
            return music
