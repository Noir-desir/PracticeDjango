from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.


def cur_time(request):

    times = datetime.datetime.now()
    # return HttpResponse('<h1>ok</h1>')
    return render(request, 'cur_time.html', {'abc':times})