from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Admin


def index(request, incorrect_data=False):
    if incorrect_data:
        return render(request, 'index/incorrect.html')
    return render(request, 'index/index.html')


def register(request):
    return render(request, 'index/register.html')


def auth(request):
    try:
        user_instance = User.objects.get(login=request.POST['login'])
        if user_instance.password.strip("'") == request.POST['password']:
            return HttpResponseRedirect(reverse('index:register'))  # Следует переписать путь до страницы с курсами
        else:
            return render(request, 'index/incorrect.html', {'login': request.POST['login']})
    except:
        try:
            admin_instance = Admin.objects.get(login=request.POST['login'])
            if admin_instance.password == request.POST['password']:
                HttpResponseRedirect(reverse('index:register'))  # Следует переписать путь до страницы админ панели
        except:
            return render(request, 'index/incorrect.html', {'login': request.POST['login']})
