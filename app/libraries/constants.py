import os

MAI_CONST = {
    'PLAYER_1P': 1,
    'PLAYER_2P': 2,
    'CHART_BASIC': 0,
    'CHART_ADVANCED': 1,
    'CHART_EXPERT': 2,
    'CHART_MASTER': 3,
    'CHART_REMASTER': 4,
}

OBS_CONST = {
    'PLAYER_1P_GENERATE_NAME': os.environ.get('PLAYER_1P_GENERATE_NAME'),
    'PLAYER_2P_GENERATE_NAME': os.environ.get('PLAYER_2P_GENERATE_NAME'),
    'PLAYER_1P_SCENE_NAME': os.environ.get('PLAYER_1P_SCENE_NAME'),
    'PLAYER_2P_SCENE_NAME': os.environ.get('PLAYER_2P_SCENE_NAME'),
    'PLAYER_1P_MASK_NAME': os.environ.get('PLAYER_1P_MASK_NAME'),
    'PLAYER_2P_MASK_NAME': os.environ.get('PLAYER_2P_MASK_NAME'),
    'PLAYER_1P_INTRO_NAME': os.environ.get('PLAYER_1P_INTRO_NAME'),
    'PLAYER_2P_INTRO_NAME': os.environ.get('PLAYER_2P_INTRO_NAME'),
}
