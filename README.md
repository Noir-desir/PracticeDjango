# PracticeDjango
## 通过视频学习Django
---
Day 1：
---
### 1. 初始化工程mysite：
    $django-admin startproject mysite
* ~manage.py ----Django项目的工具可以调用django shell和数据库
* ~settings.py ----包含了项目默认的设置，包括数据库信息，调试标志及其他一些工作的变量
* ~urls.py ----负责把URL模式映射到应用程序
### 2. 在mysite下面创建blog应用：
    $python manage.py startapp blog
### 3. 启动django项目8080端口：
    $python manage.py runserver 8080


Day 2：
---
### 1. urls.py用法（引导并创建请求地址）：
* url(参数为 正则式路径，view.py中的函数):
```python
url(r'^cur_time', views.cur_time),  
url(r'^userInfo', views.userInfo)
```
### 2. views.py用法（引导html界面，后台逻辑处理）:
* render函数(返回结果信息至html，注意格式):
```python
return render(request, 'cur_time.html', {'abc':times})  
return render(req, 'index.html', {'user_list': user_list})
```
### 3. html中循环遍历使用(模式化：引用变量使用{{}})：
```python
{% for i in user_list %}
    <tr>
        <td>{{i.username}}</td>
        <td>{{i.sex}}</td>
        <td>{{i.email}}</td>
    </tr>
{% endfor %}
```


Day 3:
---
### 1.models.py用法(数据库交互，配置字段格式)：
```python
class Userinfo(models.Model):
    username = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
```
### 2.数据库初始化前执行
    $python manage.py makemigrations
    $python manage.py migrate
### 3.写入数据库方法(在views.py中)：
```python
models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,)
```
### 4.读取数据库方法：
```python
user_list = models.UserInfo.objects.all()
```
### 5.注意检查在INSTALLED_APPS添加‘blog’，易报错
### 6.社区版pycharm数据库查看安装：
> file/setting/plugins  安装database Nivagator
