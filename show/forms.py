# -*- coding: utf-8 -*-
'''
   Project:       videoCapture
   File Name:     forms
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/4/28
   Software:      PyCharm
'''
from django import forms
class FileForm(forms.Form):
    file = forms.FileField(label="Select File ")