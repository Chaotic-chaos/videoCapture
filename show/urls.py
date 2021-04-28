# -*- coding: utf-8 -*-
'''
   Project:       videoCapture
   File Name:     urls
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/4/28
   Software:      PyCharm
'''
from django.urls import path

from show import views

urlpatterns = [
    path('', views.show_api_fake, name='show')
]
