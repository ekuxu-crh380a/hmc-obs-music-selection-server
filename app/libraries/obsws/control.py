import app.libraries.obsws.requests as OBSRequest
from app.libraries.constants import OBS_CONST, MAI_CONST
from app.libraries.functions import is_nvidia_surround
from dataclasses import dataclass
from time import sleep


@dataclass
class Player:
    maskId: int
    whiteBaseId: int
    track1GenerateId: int
    track2GenerateId: int


class OBSControl:


    def __init__(self):
        self.__player01_scene = OBS_CONST['PLAYER_1P_SCENE_NAME']
        self.__player02_scene = OBS_CONST['PLAYER_1P_SCENE_NAME'] if is_nvidia_surround() else OBS_CONST['PLAYER_2P_SCENE_NAME']

        self.__player01 = Player(0, 0, 0, 0)
        self.__player01.maskId = OBSRequest.find_item_id_by_source_name(self.__player01_scene, OBS_CONST['PLAYER_1P_MASK_NAME'])
        self.__player01.whiteBaseId = OBSRequest.find_item_id_by_source_name(self.__player01_scene, OBS_CONST['PLAYER_1P_WHITE_BASE_NAME'])
        self.__player01.track1GenerateId = OBSRequest.find_item_id_by_source_name(self.__player01_scene, OBS_CONST['PLAYER_1P_GENERATE_NAME_TRACK1'])
        self.__player01.track2GenerateId = OBSRequest.find_item_id_by_source_name(self.__player01_scene, OBS_CONST['PLAYER_1P_GENERATE_NAME_TRACK2'])
        
        self.__player02 = Player(0, 0, 0, 0)
        self.__player02.maskId = OBSRequest.find_item_id_by_source_name(self.__player02_scene, OBS_CONST['PLAYER_2P_MASK_NAME'])
        self.__player02.whiteBaseId = OBSRequest.find_item_id_by_source_name(self.__player02_scene, OBS_CONST['PLAYER_2P_WHITE_BASE_NAME'])
        self.__player02.track1GenerateId = OBSRequest.find_item_id_by_source_name(self.__player02_scene, OBS_CONST['PLAYER_2P_GENERATE_NAME_TRACK1'])
        self.__player02.track2GenerateId = OBSRequest.find_item_id_by_source_name(self.__player02_scene, OBS_CONST['PLAYER_2P_GENERATE_NAME_TRACK2'])


    def clear_all_stats(self):
        OBSRequest.set_item_disabled(self.__player01_scene, self.__player01.maskId)
        OBSRequest.set_item_disabled(self.__player01_scene, self.__player01.whiteBaseId)
        OBSRequest.set_item_disabled(self.__player01_scene, self.__player01.track1GenerateId)
        OBSRequest.set_item_disabled(self.__player01_scene, self.__player01.track2GenerateId)

        OBSRequest.set_item_disabled(self.__player02_scene, self.__player02.maskId)
        OBSRequest.set_item_disabled(self.__player02_scene, self.__player02.whiteBaseId)
        OBSRequest.set_item_disabled(self.__player02_scene, self.__player02.track1GenerateId)
        OBSRequest.set_item_disabled(self.__player02_scene, self.__player02.track2GenerateId)


    def toggle_player_mask(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = self.__player01_scene
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = self.__player02_scene
                control = self.__player02
            OBSRequest.toggle_item_enabled(scene, control.maskId)

    
    def show_player_selection(self, player: int, track: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = self.__player01_scene
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = self.__player02_scene
                control = self.__player02
            if track == 1:
                OBSRequest.set_item_enabled(scene, control.whiteBaseId)
                OBSRequest.set_item_enabled(scene, control.track1GenerateId)
                OBSRequest.set_item_disabled(scene, control.track2GenerateId)
            elif track == 2:
                OBSRequest.set_item_enabled(scene, control.whiteBaseId)
                OBSRequest.set_item_enabled(scene, control.track2GenerateId)
                OBSRequest.set_item_disabled(scene, control.track1GenerateId)


    def hide_player_selection(self, player: int):
        if player == MAI_CONST['PLAYER_1P'] or player == MAI_CONST['PLAYER_2P']:
            if player == MAI_CONST['PLAYER_1P']:
                scene = self.__player01_scene
                control = self.__player01
            elif player == MAI_CONST['PLAYER_2P']:
                scene = self.__player02_scene
                control = self.__player02
            OBSRequest.set_item_disabled(scene, control.track1GenerateId)
            OBSRequest.set_item_disabled(scene, control.track2GenerateId)
            OBSRequest.set_item_disabled(scene, control.whiteBaseId)


class TimingControl:

    
    def __init__(self):
        self.__ctrl = OBSControl()


    def init_screen(self):
        self.__ctrl.clear_all_stats()


    def show_player_selection(self, player: int, track: int):
        self.__ctrl.toggle_player_mask(player)
        sleep(1)
        self.__ctrl.show_player_selection(player, track)
        sleep(2)
        self.__ctrl.toggle_player_mask(player)


    def clear_player_selection(self):
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_1P'])
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_2P'])
        sleep(1)
        self.__ctrl.hide_player_selection(MAI_CONST['PLAYER_1P'])
        self.__ctrl.hide_player_selection(MAI_CONST['PLAYER_2P'])
        sleep(2)
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_1P'])
        self.__ctrl.toggle_player_mask(MAI_CONST['PLAYER_2P'])
