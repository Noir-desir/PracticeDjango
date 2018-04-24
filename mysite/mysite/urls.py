"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^cur_time', views.cur_time),
    # url(r'^userInfo', views.userInfo),

#no named group 无名参数
    # url(r'^articles/2003/$', views.special_case_2003),
    # url(r'^articles/2003/', views.special_case_2003),

    # url(r'^articles/[0-9]{4}/$', views.year_archive),
    # url(r'^articles/([0-9]{4})/$', views.year_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.year_archive),
#named group 有名参数
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_archive),
# 别名
    # url(r'^index', views.index, name="alex")
# urls分发
    url(r'^blog/', include('blog.urls')),
]
