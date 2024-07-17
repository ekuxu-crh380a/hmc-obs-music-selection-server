import app.libraries.obsws.requests as OBSRequest
from app.libraries.constants import OBS_CONST, MAI_CONST
from dataclasses import dataclass
from time import sleep


@dataclass
class Player:
    maskId: int
    generateId: int


class OBSControl:


    def __init__(self):
        self.__player01 = Player(0, 0)
        self.__player01.maskId = OBSRequest.find_item_id_by_source_name(OBS_CONST['PLAYER_1P_SCENE_NAME'], OBS_CONST['PLAYER_1P_MASK_NAME'])
        self.__player01.generateId = OBSRequest.find_item_id_by_source_name(OBS_CONST['PLAYER_1P_SCENE_NAME'], OBS_CONST['PLAYER_1P_GENERATE_NAME'])
        self.__player02 = Player(0, 0)
        self.__player02.maskId = OBSRequest.find_item_id_by_source_name(OBS_CONST['PLAYER_2P_SCENE_NAME'], OBS_CONST['PLAYER_2P_MASK_NAME'])
        self.__player02.generateId = OBSRequest.find_item_id_by_source_name(OBS_CONST['PLAYER_2P_SCENE_NAME'], OBS_CONST['PLAYER_2P_GENERATE_NAME'])


    async def clear_all_stats(self):
        OBSRequest.set_item_disabled(OBS_CONST['PLAYER_1P_SCENE_NAME'], self.__player01.maskId)
        OBSRequest.set_item_disabled(OBS_CONST['PLAYER_1P_SCENE_NAME'], self.__player01.generateId)
        OBSRequest.set_item_disabled(OBS_CONST['PLAYER_1P_SCENE_NAME'], self.__player02.maskId)
        OBSRequest.set_item_disabled(OBS_CONST['PLAYER_1P_SCENE_NAME'], self.__player02.generateId)


    async def toggle_player_mask(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = OBS_CONST['PLAYER_1P_SCENE_NAME']
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = OBS_CONST['PLAYER_2P_SCENE_NAME']
                control = self.__player02
            OBSRequest.toggle_item_enabled(scene, control.maskId)
            sleep(3.5)
            OBSRequest.set_item_disabled(scene, control.maskId)

    
    async def show_player_selection(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = OBS_CONST['PLAYER_1P_SCENE_NAME']
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = OBS_CONST['PLAYER_2P_SCENE_NAME']
                control = self.__player02
            OBSRequest.set_item_enabled(scene, control.generateId)


    async def hide_player_selection(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = OBS_CONST['PLAYER_1P_SCENE_NAME']
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = OBS_CONST['PLAYER_2P_SCENE_NAME']
                control = self.__player02
            OBSRequest.set_item_disabled(scene, control.generateId)

    
    async def toggle_player_selection(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = OBS_CONST['PLAYER_1P_SCENE_NAME']
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = OBS_CONST['PLAYER_2P_SCENE_NAME']
                control = self.__player02
            OBSRequest.toggle_item_enabled(scene, control.generateId)


class TimingControl:

    
    def __init__(self):
        self.__ctrl = OBSControl()


    async def show_player_selection(self, player: int):
        self.__ctrl.toggle_player_mask(player)
        await sleep(1)
        self.__ctrl.show_player_selection(player)


    async def clear_player_selection(self):
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_1P'])
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_2P'])
        await sleep(1)
        self.__ctrl.hide_player_selection(MAI_CONST['PLAYER_1P'])
        self.__ctrl.hide_player_selection(MAI_CONST['PLAYER_2P'])
