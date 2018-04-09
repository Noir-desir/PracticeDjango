from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.


def cur_time(request):

    times = datetime.datetime.now()
    # return HttpResponse('<h1>ok</h1>')
    return render(request, 'cur_time.html', {'abc':times})


user_list = []


def userInfo(req):
    if req.method == 'POST':
        username = req.POST.get('username', None)
        sex = req.POST.get('sex', None)
        email = req.POST.get('email', None)
        user = {'username': username, 'sex': sex,'email': 'email'}
        user_list.append(user)

        # return  render(req, 'index.html', {'user_list': user_list})
        # print(username, sex, email)
    return render(req, 'index.html', {'user_list': user_list})
