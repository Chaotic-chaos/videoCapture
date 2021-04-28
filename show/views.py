import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from show.models import Video


def show_api_fake(request):
    params = json.loads(request.body)
    video_name = params['video_name']
    try:
        video = get_object_or_404(Video, video_name=video_name)
    except Exception as e:
        return HttpResponse(404)
    # print(video)
    # print(video.video_summary)
    return HttpResponse(video.video_summary)