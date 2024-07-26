from app.settings import DATA_DIR
from PIL import Image, ImageDraw, ImageFont
from app.libraries.maimusic import id2music
from app.libraries.maicover.functions import truncate_text, get_cover_path
from app.libraries.constants import MAI_CONST, OBS_CONST
from typing import Dict


def generate_cover(player: int, track: int, music: Dict) -> bool:
    difficulty = music['difficulty']
    level_list = ['ba','ad','ex','ma','re']
    level = level_list[int(difficulty)]

    baseImg = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    baseImgDraw = ImageDraw.Draw(baseImg)


    backageImg = Image.open(f"{DATA_DIR}/assets/images/BASE.png").convert('RGBA')
    baseImg.paste(backageImg,(0,0),backageImg.split()[3])

    BaseCoverImg = Image.open(get_cover_path(music['id'])).convert('RGBA')
    BaseCoverImg = BaseCoverImg.resize((1080,1080))
    baseImg.paste(BaseCoverImg,(0,840),BaseCoverImg.split()[3])
                
    fx = Image.open(f"{DATA_DIR}/assets/images/FX.png").convert('RGBA')
    fx = fx.resize((1080,1080))
    baseImg.paste(fx,(0,840),fx.split()[3])
                
    mask = Image.open(f"{DATA_DIR}/assets/images/mask.png").convert('RGBA')
    mask = mask.resize((1080,1920))
    baseImg.paste(mask,(0,0),mask.split()[3])

    wrap_list_dx = [0,0,-1,2,3]
    wrap_list_sd = [0,0,3,7,3]

    Base_Cover = Image.open(f"{DATA_DIR}/assets/images/{level}/Base.png").convert('RGBA')
    if music['type'] == 'DX':
        base_tab = Image.open(f"{DATA_DIR}/assets/images/{level}/DX_TAB.png").convert('RGBA')
        wrap = wrap_list_dx[difficulty]
    else:
        base_tab = Image.open(f"{DATA_DIR}/assets/images/{level}/SD_TAB.png").convert('RGBA')
        wrap = wrap_list_sd[difficulty]
    baseImg.paste(Base_Cover,(287,1067),Base_Cover.split()[3])
    baseImg.paste(base_tab,(284+wrap,982),base_tab.split()[3])

    CoverImg = Image.open(get_cover_path(music['id'])).convert('RGBA')
    CoverImg = BaseCoverImg.resize((417,417))
    baseImg.paste(CoverImg,(335,1102),CoverImg.split()[3])

    level_num = str(music['level'])
    level = Image.open(f"{DATA_DIR}/assets/images/{level}/{level_num}.png").convert('RGBA')
    baseImg.paste(level,(637,1535),level.split()[3])

    tempFont = ImageFont.truetype(f'{DATA_DIR}/assets/fonts/A-OTF-UDShinGoPr6N-Bold.otf', 30, encoding='utf-8')
    title = truncate_text(music['title'], tempFont, 400)
    text_width, text_height = tempFont.getsize(str(title))
    baseImgDraw.text(((540-text_width/2),(1650-text_height/2)), title , "white" , tempFont)

    tempFont = ImageFont.truetype(f"{DATA_DIR}/assets/fonts/A-OTF-UDShinGoPr6N-Regular.otf", 23, encoding='utf-8')
    artist = truncate_text(music['artist'], tempFont, 400)
    text_width, text_height = tempFont.getsize(str(artist))
    baseImgDraw.text(((540-text_width/2),(1712-text_height/2)), artist , "white" , tempFont)

    if player == MAI_CONST['PLAYER_1P']:
        if track == 1:
            baseImg.save(f"{OBS_CONST['PLAYER_SELECTION_GENERATE_PATH']}/{OBS_CONST['PLAYER_1P_GENERATE_NAME_TRACK1']}.png")
            return True
        elif track == 2:
            baseImg.save(f"{OBS_CONST['PLAYER_SELECTION_GENERATE_PATH']}/{OBS_CONST['PLAYER_1P_GENERATE_NAME_TRACK2']}.png")
            return True
        return False
    elif player == MAI_CONST['PLAYER_2P']:
        if track == 1:
            baseImg.save(f"{OBS_CONST['PLAYER_SELECTION_GENERATE_PATH']}/{OBS_CONST['PLAYER_2P_GENERATE_NAME_TRACK1']}.png")
            return True
        elif track == 2:
            baseImg.save(f"{OBS_CONST['PLAYER_SELECTION_GENERATE_PATH']}/{OBS_CONST['PLAYER_2P_GENERATE_NAME_TRACK2']}.png")
            return True
        return False
    return False
