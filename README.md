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


Day 4：
---
### 1. wsgi服务器了解一下
### 2. Django建数据库内部流程:
> 1. settings.py读取`INSTALLED_APPS['blog']`
> 2. blog文件夹下面的models.py读取创建的类`class UserInfo(models.Model):`
### 3. settings用法(前端等文件配置):
1. 网页模板文件夹路径：
 ```python
TEMPLATES = [
{
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
}]
```
2. 静态文件夹路径（图片,JS等）：
 ```python
STATIC_URL = '/abc/'  #设置路径别名链接，文件移动只用修改下面绝对路径

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics"),  #静态文件路径,一般在CDN上
     
)
```
注意：元组后面的','必须带上  
3. for example：
```html
<script src="/abc/js/jquery-3.3.1.min.js"></script>
<script>
    $("h1").css("color","red")
</script>
```
注意：路径前必须必须带上'/'

Day 5：
---
## Django URL (路由系统)
```
urlpatterns = [
    url(正则表达式, views视图函数，参数，别名),
]
```
> 参数说明：
- 一个正则表达式字符串
- 一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
- 可选的要传递给视图函数的默认参数（字典形式）
- 一个可选的name参数
### 1. URL连接
```python
 url(r'^articles/2003/$', views.special_case_2003),
 #正则表达式的严格起止匹配
 url(r'^articles/[0-9]{4}/', views.year_archive),
 #4位数字后面可以接任何字符均跳转到views.year_archive
```
### 2. 截取URL中参数
- 无名参数（使用正则式中括号确定参数）
```python
url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.year_archive),
```
**注**：视图函数views.py 中根据***传参位置***来截取字符串
```python
def year_archive(req, y, m):

    return HttpResponse(y+'year'+m+'month')
```
- 有名参数( `(?P<year>[0-9]{4})` )
```python
url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_archive),
```
**注**：视图函数views.py 中根据***制定名称***来截取字符串 
```python
def year_archive(req, year, month):

    return HttpResponse(year+'year'+month+'month')
```
### 3. URL别名
（为了防止后台多次更改url地址）
for example：
```python
url(r'^index', views.index, name="alex")
```
- views.py中后台处理：
```python
def index(req):
    if req.method == "POST":
        ###
        return HttpResponse('登录成功')
    ###
    return render(req, "login.html")
```
- login.html前台展示：
> {% url "alex" %} Django固定模板
```html
<form action={% url "alex" %} method="post">
<input type="text" name="username">
<input type="password" name="pwd">
<input type="submit" value="submit">
```
Day 6：
---
### 4. 分发urls.py到各个APP
(为了让各个APP业务独立出来)
- 引入include
```python
    from django.conf.urls import url, include

```
- 在根目录中的urls.py中添加(url分发到APP目录)
```python
    url(r'^blog/', include('blog.urls')),
```
- APP目录中新建urls.py，独立使用urls.py
```python
    url(r'new/story', views.introduce),
```
(在blog文件夹中的urls.py不能使用'^'为开头，因为根目录下的blog才是固定开头)

Day 7：
---
## Django Views (视图函数)
### 1. HttpRequest对象的属性和方法
- **path**  返回请求页面的全路径，不包括域名
```python
    print("req.path", req.path)
```
> req.path /blog/pay/index
- **method**  请求中使用的HTTP方法的字符串表示。全大写表示
```python
    if req.method == "POST":
```
> 判断请求方法是不是POST（GET）
- **GET**  包含所有HTTP GET**参数**的类字典对象
```python
    print("req.GET", req.GET)
```
> req.GET <QueryDict: {}>
- **POST**  包含所有HTTP POST**参数**的类字典对象
- **COOKIES**  包含所有cookies的标准Python字典对象；keys和values都是字符串
- **FILES**   包含所有上传文件的类字典对象；
FILES中的每一个Key都是`<input type="file" name="" />`标签中name属性的值，
FILES中的每一个value同时也是一个标准的python字典对象，
包含下面三个Keys：
    + filename：      上传文件名，用字符串表示
    + content_type:   上传文件的Content Type
    + content：       上传文件的原始内容