from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
from blog import models

def cur_time(request):

    times = datetime.datetime.now()
    # return HttpResponse('<h1>ok</h1>')
    return render(request, 'cur_time.html', {'abc':times})


# user_list = []


def userInfo(req):
    if req.method == 'POST':
        u = req.POST.get('username', None)
        s = req.POST.get('sex', None)
        e = req.POST.get('email', None)
        # user = {'username': username, 'sex': sex,'email': email}
        # user_list.append(user)

        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,

        )

    user_list = models.UserInfo.objects.all()

    return render(req, 'index.html', {'user_list': user_list})
