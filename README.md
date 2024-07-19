# 贺州舞萌 DX 比赛选曲 OBS 控制器（后端）

# 说明

基于 `obsws-python` SDK 与本地 OBS Studio 通信，通过预编好的场景动效实现选手台上曲目展示的演出效果。

运行DEMO：[https://www.bilibili.com/video/BV1YW42197LT](https://www.bilibili.com/video/BV1YW42197LT)

# 安装及运行

1. 通过 `git clone` 或下载代码包到本地。
2. 进入项目目录，使用 `pip install -r requirements.txt` 下载所需依赖。
3. 通过 [此链接](#) 下载图片资源包，放入项目的 `data` 目录中。
4. 复制一份 `example.env` 并重命名为 `.env`，打开并将配置修改成您本地的 OBS WebSocket 连接配置和场景名称。
5. 通过 `python manage.py runserver` 启动服务。
6. 使用任意 WebSocket 客户端，连接 `ws://<your_ip>:8000/ws/obs_control/` .
7. 按照 [请求体](#请求体) 和 [接口列表](#接口列表) 执行请求，即可完成 OBS Studio 的控制。

# 请求与响应

## 1. 请求体

``` JSON
{
    "mode": "request",             // 此处固定为 "request"
    "endpoint": "<endpoint>",      // 此处为 WebSocket 请求的业务端点，详见接口列表
    "data": {                      // 此处为请求参数（部分接口无额外参数，留空即可）
        "some_data": "some_value",
        ......
    }
}
```

## 2. 响应体

``` JSON
{
    "mode": "response",            // 此处固定为 "response"
    "endpoint": "<endpoint>",      // 此处为 WebSocket 请求的业务端点，详见接口列表
    "data": {                      // 此处为返回数据
        "some_data": "some_value",
        ......
    }
}
```

## 3. 错误响应体

``` JSON
{
    "mode": "error",               // 此处固定为 "error"
    "endpoint": "<endpoint>",      // 此处为 WebSocket 请求的业务端点，详见接口列表
    "data": {
        "message": "error_message" // 此处为错误信息
    }
}
```

# 接口列表

## 1. `get_music_list`

### 功能

查询曲库中的所有歌曲信息。

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`music_list`|`List<Object>`|含有曲目 ID 、名称、艺术家、等级、谱面类型、难度的数据对象列表|

#### `Object`

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`id`|`str`|曲目 ID|
|`title`|`str`|曲目名称|
|`artist`|`str`|艺术家|
|`type`|`str`|谱面类型（标准、DX）|
|`level`|`List<str>`|谱面难度（BASIC、ADVANCED、EXPERT、MASTER、Re:MASTER）|

## 2. `get_music_info`

### 功能

通过曲目 ID 查询曲库中的歌曲信息。

### 请求参数

|参数名称|类型|参数说明|
|:-----:|:-------:|:-------:|
|`music_id`|`str`|曲目ID|

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`music_info`|`Object`|含有曲目 ID 、名称、艺术家、等级、谱面类型、难度的数据对象|

#### `Object music_info`

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`id`|`str`|曲目 ID|
|`title`|`str`|曲目名称|
|`artist`|`str`|艺术家|
|`type`|`str`|谱面类型（标准、DX）|
|`level`|`List<str>`|谱面难度（BASIC、ADVANCED、EXPERT、MASTER、Re:MASTER）|

## 3. `build_player01_selection`

### 功能

构建 1P 玩家选曲图。

### 请求参数

|参数名称|类型|参数说明|
|:-----:|:-------:|:-------:|
|`music_id`|`str`|曲目ID|
|`difficulty`|`int`|难度索引|

此处的 `difficulty` 取值为：BASIC = `0`，ADVANCED = `1`，EXPERT = `2`，MASTER = `3`，Re:MASTER = `4`.

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|构建进程中的实时返回信息|

## 4. `build_player02_selection`

### 功能

构建 2P 玩家选曲图。

### 请求参数

|参数名称|类型|参数说明|
|:-----:|:-------:|:-------:|
|`music_id`|`str`|曲目ID|
|`difficulty`|`int`|难度索引|

此处的 `difficulty` 取值为：BASIC = `0`，ADVANCED = `1`，EXPERT = `2`，MASTER = `3`，Re:MASTER = `4`.

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|构建进程中的实时返回信息|

## 5. `init_screen`

### 功能

初始化双方选曲屏幕，进入待机屏画面。

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|切换场景进程中的实时返回信息|

## 6. `show_player01_selection`

### 功能

显示 1P 玩家的选曲。

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|切换场景进程中的实时返回信息|

## 7. `show_player02_selection`

### 功能

显示 2P 玩家的选曲。

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|切换场景进程中的实时返回信息|

## 8. `clear_player_selection`

### 功能

清除双方选曲，返回待机屏画面。

### 返回数据

|数据名称|类型|数据说明|
|:-----:|:-------:|:-------:|
|`message`|`str`|切换场景进程中的实时返回信息|

# LICENSE

(C) 2024 HMT - Hezhou mai Team, build with LOVE & PASSION by KIO & 3.80GHz, under MIT License.
