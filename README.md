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