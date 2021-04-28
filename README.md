## Api

### 视频名称 -> 视频总结

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