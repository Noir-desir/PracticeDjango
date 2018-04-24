#!/usr/bin/env python
# encoding: utf-8
"""
@author: ‘jiangzeyu‘
@time: 2018/4/24 21:51
"""

from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'new/story', views.introduce),
]