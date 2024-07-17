import obsws_python as obsws
from typing import Dict
from app.settings import OBS_WS_HOST, OBS_WS_PASSWORD, OBS_WS_PORT, OBS_WS_TIMEOUT


class OBSClient():

   
    ''' OBS Websocket Client

        Description: OBS-Websocket 接口调用封装
    '''


    def __init__(self):
        
        ''' 构造函数

            Description: 
                与 OBS-Websocket 服务器建立连接。
                OBS-Websocket 服务器配置从 .env 文件中获取。
        '''

        self.__client = obsws.ReqClient(host = OBS_WS_HOST, port = int(OBS_WS_PORT),
            password = OBS_WS_PASSWORD, timeout = int(OBS_WS_TIMEOUT))


    def get_version(self) -> Dict:

        ''' 获取版本信息

            Description:
                获取当前操作系统的环境和 OBS 程序的版本信息。

            Return:
                - <Dict> 含操作系统环境和 OBS 程序版本信息的字典
        '''

        res = self.__client.get_version()
        return {
            'OBSVersion': res.obs_version,
            'OBSWebSocketVersion': res.obs_web_socket_version,
            'RPCVersion': res.rpc_version,
            'Platform': res.platform,
            'PlatformDescription': res.platform_description,
        }


    def set_scene(self, scene_name: str):

        ''' 切换 OBS 场景（模板）

            Description:
                切换 OBS 场景模板，如单人机位画面或双人机位画面。

            Parameters:
                - scene_name: str 场景模板名称
        '''

        self.__client.set_current_program_scene(scene_name)


    def get_scene_item_list(self, scene_name: str):
        res = self.__client.get_scene_item_list(scene_name)
        return res.scene_items
    

    def get_scene_item_enabled(self, scene_name: str, item_id: int):
        res = self.__client.get_scene_item_enabled(scene_name, item_id)
        return res.scene_item_enabled
    

    def set_scene_item_enabled(self, scene_name: str, item_id: int, enabled: bool):
        self.__client.set_scene_item_enabled(scene_name, item_id, enabled)
