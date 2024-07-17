from app.settings import DATA_DIR
from PIL import Image, ImageDraw, ImageFont
from app.libraries.maimusic import id2music
from app.libraries.maicover.functions import truncate_text, get_cover_path
from app.libraries.constants import MAI_CONST, OBS_CONST


def generate_cover(player: int, music_id: int, difficulty: int) -> bool:
    
    music_info = id2music(str(music_id))

    baseImg = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    baseImgDraw = ImageDraw.Draw(baseImg)


    backageImg = Image.open(f"{DATA_DIR}/assets/images/BASE.png").convert('RGBA')
    baseImg.paste(backageImg,(0,0),backageImg.split()[3])

    BaseCoverImg = Image.open(get_cover_path(music_id)).convert('RGBA')
    BaseCoverImg = BaseCoverImg.resize((1080,1080))
    baseImg.paste(BaseCoverImg,(0,840),BaseCoverImg.split()[3])
            
    fx = Image.open(f"{DATA_DIR}/assets/images/FX.png").convert('RGBA')
    fx = fx.resize((1080,1080))
    baseImg.paste(fx,(0,840),fx.split()[3])
            
    mask = Image.open(f"{DATA_DIR}/assets/images/mask.png").convert('RGBA')
    mask = mask.resize((1080,1920))
    baseImg.paste(mask,(0,0),mask.split()[3])

    wrap = 0
    if difficulty == MAI_CONST['CHART_MASTER']:
        Base_Cover = Image.open(f"{DATA_DIR}/assets/images/Base_MST.png").convert('RGBA')
        if music_info['type'] == 'DX':
            base_tab = Image.open(f"{DATA_DIR}/assets/images/DX_TAB_MS.png").convert('RGBA')
        else:
            base_tab = Image.open(f"{DATA_DIR}/assets/images/SD_TAB_MS.png").convert('RGBA')
            wrap = 5
        level_num = str(music_info['level'][3])
        baseImg.paste(Base_Cover,(285,1065),Base_Cover.split()[3])
    elif difficulty == MAI_CONST['CHART_REMASTER']:
        Base_Cover = Image.open(f"{DATA_DIR}/assets/images/Base_REM.png").convert('RGBA')
        if music_info['type'] == 'DX':
            wrap = 3
            base_tab = Image.open(f"{DATA_DIR}/assets/images/DX_TAB_RE.png").convert('RGBA')
        else:
            wrap = 3
            base_tab = Image.open(f"{DATA_DIR}/assets/images/SD_TAB_RE.png").convert('RGBA')
        level_num = str(music_info['level'][4])  
        baseImg.paste(Base_Cover,(287,1067),Base_Cover.split()[3])
    baseImg.paste(base_tab,(284+wrap,982),base_tab.split()[3])

    CoverImg = Image.open(get_cover_path(music_id)).convert('RGBA')
    CoverImg = BaseCoverImg.resize((417,417))
    baseImg.paste(CoverImg,(335,1102),CoverImg.split()[3])

    level = Image.open(f"{DATA_DIR}/assets/images/{level_num}.png").convert('RGBA')
    baseImg.paste(level,(637,1535),level.split()[3])

    tempFont = ImageFont.truetype(f'{DATA_DIR}/assets/fonts/A-OTF-UDShinGoPr6N-Bold.otf', 30, encoding='utf-8')
    title = truncate_text(music_info['title'], tempFont, 800)
    text_width, text_height = tempFont.getsize(str(title))
    baseImgDraw.text(((540-text_width/2),(1650-text_height/2)), title , "white" , tempFont)

    tempFont = ImageFont.truetype(f"{DATA_DIR}/assets/fonts/A-OTF-UDShinGoPr6N-Regular.otf", 23, encoding='utf-8')
    artist = truncate_text(music_info["basic_info"]['artist'], tempFont, 800)
    text_width, text_height = tempFont.getsize(str(artist))
    baseImgDraw.text(((540-text_width/2),(1712-text_height/2)), artist , "white" , tempFont)

    if player == MAI_CONST['PLAYER_1P']:
        baseImg.save(f"{DATA_DIR}/cover-generated/{OBS_CONST['PLAYER_1P_GENERATE_NAME']}.png")
        return True
    elif player == MAI_CONST['PLAYER_2P']:
        baseImg.save(f"{DATA_DIR}/cover-generated/{OBS_CONST['PLAYER_2P_GENERATE_NAME']}.png")
        return True
    return False
