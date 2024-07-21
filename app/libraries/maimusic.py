from app.settings import DATA_DIR
import json


def id2music(id):
    with open(f"{DATA_DIR}/music_data.json", 'r', encoding='utf-8') as file:
        music_data = json.load(file)
    for music in music_data:
        if id == music["id"]:
            return music
        

def musiclist():
    with open(f"{DATA_DIR}/music_data.json", 'r', encoding='utf-8') as file:
        return json.load(file)
