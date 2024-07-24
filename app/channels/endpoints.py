from app.channels.response import response, error, send
from app.libraries.maimusic import id2music, musiclist
from app.libraries.maicover.generator import generate_cover
from app.libraries.obsws.control import TimingControl
from app.libraries.constants import MAI_CONST
from typing import Dict


class WebSocketEndpoint:


    @staticmethod
    def get_music_list(ws, request: Dict) -> bool:
        music_list = []
        raw = musiclist()
        if 'level' in request.keys():
            for music in raw:
                if music['level'] == request['level']:
                    music_list.append(music)
        else:
            for music in raw:
                    music_list.append(music)
        send(ws, response('get_music_list', {
            'music_list': music_list,
        }))
        return True


    @staticmethod
    def get_music_info(ws, request: Dict) -> bool:
        if 'music_id' not in request or 'difficulty' not in request:
            send(ws, error('get_music_info', f'请指定曲目ID和难度'))
            return False
        if request['difficulty'] > 4:
            send(ws, error('get_music_info', f'难度索引不符合要求，请重新提交'))
            return False
        music = id2music(request['music_id'], request['difficulty'])
        if not music:
            send(ws, error('get_music_info', f"未找到 ID = {request['music_id']} 的曲目信息"))
            return False
        send(ws, response('get_music_info', {
            'music_info': music,
        }))
        return True
    

    @staticmethod
    def build_player01_selection(ws, request: Dict) -> bool:
        if 'music_id' not in request or 'difficulty' not in request:
            send(ws, error('build_player01_selection', f'请指定曲目ID和难度'))
            return False
        if request['difficulty'] > 4:
            send(ws, error('build_player01_selection', f'难度索引不符合要求，请重新提交'))
            return False
        music = id2music(request['music_id'], request['difficulty'])
        if not music:
            send(ws, error('build_player01_selection', f"未找到 ID = {request['music_id']} 的曲目信息"))
            return False
        send(ws, response('build_player01_selection', {
            'message': '正在处理1P选曲图......'
        }))
        if not generate_cover(MAI_CONST['PLAYER_1P'], music):
            send(ws, error('build_player01_selection', f"1P选取图生成失败！请查看日志文件查找原因"))
            return False
        send(ws, response('build_player01_selection', {
            'message': '1P选曲图生成完成！'
        }))
        return True
        

    
    @staticmethod
    def build_player02_selection(ws, request: Dict) -> bool:
        if 'music_id' not in request or 'difficulty' not in request:
            send(ws, error('build_player02_selection', f'请指定曲目ID和难度'))
            return False
        if request['difficulty'] > 4:
            send(ws, error('build_player02_selection', f'难度索引不符合要求，请重新提交'))
            return False
        music = id2music(request['music_id'], request['difficulty'])
        if not music:
            send(ws, error('build_player02_selection', f"未找到 ID = {request['music_id']} 的曲目信息"))
            return False
        send(ws, response('build_player02_selection', {
            'message': '正在处理2P选曲图......'
        }))
        if not generate_cover(MAI_CONST['PLAYER_2P'], music):
            send(ws, error('build_player02_selection', f"2P选取图生成失败！请查看日志文件查找原因"))
            return False
        send(ws, response('build_player02_selection', {
            'message': '2P选曲图生成完成！'
        }))
        return True

    
    @staticmethod
    def init_screen(ws, request: Dict) -> bool:
        send(ws, response('init_screen', {
            'message': '正在初始化屏幕......'
        }))
        control = TimingControl()
        control.init_screen()
        send(ws, response('init_screen', {
            'message': '初始化屏幕完毕！'
        }))
        return True
    

    @staticmethod
    def show_player01_selection(ws, request: Dict) -> bool:
        send(ws, response('show_player01_selection', {
            'message': '正在展示1P选曲......'
        }))
        control = TimingControl()
        control.show_player_selection(MAI_CONST['PLAYER_1P'])
        send(ws, response('show_player01_selection', {
            'message': '1P选曲展示完成！'
        }))
        return True
    

    @staticmethod
    def show_player02_selection(ws, request: Dict) -> bool:
        send(ws, response('show_player02_selection', {
            'message': '正在展示2P选曲......'
        }))
        control = TimingControl()
        control.show_player_selection(MAI_CONST['PLAYER_2P'])
        send(ws, response('show_player02_selection', {
            'message': '2P选曲展示完成！'
        }))
        return True
    

    @staticmethod
    def clear_player_selection(ws, request: Dict) -> bool:
        send(ws, response('clear_player_selection', {
            'message': '清除双方选曲中......'
        }))
        control = TimingControl()
        control.clear_player_selection()
        send(ws, response('clear_player_selection', {
            'message': '清除选曲完成，已返回主屏幕！'
        }))
        return True
