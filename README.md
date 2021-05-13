## Api

### 上传自定义视频 -> 视频描述

#### Method

> POST

#### URL

> http://10.103.14.65:1111/show/upload/

#### Parameters

- 参数格式：`form-data`

- 参数：

  ```json
  "file": <要上传的视频文件>
  ```

  

#### Response

```json
{
	"video": "<前端页面进行视频渲染的预留字段，客户端用不到>",
	"summary": "<上传的视频描述>",
	"tts_audio": "<base64编码过后的wav音频>"
}
```



### 服务端缓存好的视频特征 -> 视频描述

#### Method

> GET

#### URL

> http://10.103.14.65:1111/show/model_decode/<video_id>

#### Parameters

> video_id: 纯数字，直接拼接在url后面即可

#### Response

```json
{
	"summary": "<视频描述>",
	"video_file": "<原视频路径，头部拼接服务URL即可访问视频>",
	"audio": "<base64编码后的音频>"
}
```



### 视频名称 -> 视频描述

#### Method

> POST

#### URL

> http://49.234.127.192:1111/show/showApiFake/

#### Parameters

```json
{
    "video_name": "<video_name>"
}
```

#### Response

```json
# 存在该视频
Two men are playing table tennis game.

# 不存在该视频
404
```



## 前端页面使用

### URL

> http://49.234.127.192:1111/show/index

### Notes

1. 目前只支持数据库内已经有的