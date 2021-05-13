# -*- coding: utf-8 -*-
'''
   Project:       videoCapture
   File Name:     urls
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/4/28
   Software:      PyCharm
'''
from django.urls import path, re_path
from django.views.static import serve

from show import views
from videoCapture import settings

app_name = 'show'
urlpatterns = [
    path('showApiFake/', views.show_api_fake, name='show'),
    path('index/', views.index, name='index'),
    path('showWeb/<file_name>', views.show_web_fake, name='showWeb'),
    path('upload/', views.upload, name='upload_video'),
    path('model_decode/<video_id>', views.get_model_decode, name="get_model_decode"),
    re_path(r'uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
