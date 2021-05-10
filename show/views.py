import json
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tts.v20190823 import tts_client, models

from show.forms import FileForm
from show.models import Video
from videoCapture.settings import BASE_DIR, SECRETID, SECRETKEY


def show_api_fake(request):
    '''一个假的api，给定视频名称返回对应总结文本'''
    params = json.loads(request.body)
    video_name = params['video_name']
    try:
        video = get_object_or_404(Video, video_name=video_name)
    except Exception as e:
        return HttpResponse(404)
    # print(video)
    # print(video.video_summary)
    return HttpResponse(video.video_summary)

def save_video_and_get_summary(input_file):
    # get file name
    video_name = input_file.name
    # save file
    with open(f'uploads/{video_name}', 'wb') as destination:
        for chunk in input_file.chunks():
            destination.write(chunk)

    return video_name

def index(request):
    if request.method == 'POST':
        # 携带数据进行后续处理
        form = FileForm(request.body, request.FILES)
        video_name = save_video_and_get_summary(request.FILES['file'])
        return redirect("show:showWeb", file_name=video_name)
    else:
        form = FileForm()
        return render(request, "show/index.html", {'form': form})

def show_web_fake(request, file_name):
    '''一个假的前端页面，给定上传视频名称及路径，自动提取文件名并查表返回视频总结同时渲染播放页面'''
    query_key = file_name.split('.')[0]
    try:
        video = get_object_or_404(Video, video_name=query_key)
    except Exception as e:
        print(e)
        return render(request, "show/play.html", {'status': 404})

    # tts
    try:
        cred = credential.Credential(SECRETID, SECRETKEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tts.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tts_client.TtsClient(cred, "ap-nanjing", clientProfile)

        req = models.TextToVoiceRequest()
        params = {
            "Text": video.video_summary,
            "SessionId": "55555",
            "ModelType": 1,
            "VoiceType": 4,
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextToVoice(req)
        # print(resp.to_json_string())
        tts_audio = f"data:audio/wav;base64,{json.loads(resp.to_json_string())['Audio']}"

    except TencentCloudSDKException as err:
        tts_audio = 404

    return render(request, "show/play.html", {
        "status": 200,
        "video": f"uploads/{file_name}",
        "summary": video.video_summary,
        "tts_audio": tts_audio,
    })