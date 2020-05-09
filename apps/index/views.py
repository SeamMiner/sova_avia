from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import User, Admin


def index(request, incorrect_data=0):
    if incorrect_data:
        return render(request, 'index/incorrect.html')
    return render(request, 'index/index.html')


def register(request, unfortunately=None):
    if unfortunately is None:
        return render(request, 'index/register.html')
    if unfortunately:
        return render(request, 'index/incorrect_reg.html')
    return render(request, 'index/incorrect_password.html')


def auth(request):
    try:
        user_instance = User.objects.get(login=request.POST['login'])
        if user_instance.password == request.POST['password']:
            return HttpResponseRedirect(reverse('index:register'))  # Следует переписать путь до страницы с курсами
        else:
            return HttpResponseRedirect(reverse('index:index', args=(1, )))
    except:
        try:
            admin_instance = Admin.objects.get(login=request.POST['login'])
            if admin_instance.password == request.POST['password']:
                return HttpResponseRedirect(reverse('index:register'))  # Следует переписать путь до страницы админ панели
        except:
            return HttpResponseRedirect(reverse('index:index', args=(1, )))


def new(request):
    try:
        current_password = request.POST['password0']
        if current_password == request.POST['password1']:
            current_login = request.POST['login']
            for admin in Admin.objects.all():
                if admin.login == current_login:
                    break
            else:
                Admin.objects.create(login=current_login, password=current_password)
                return HttpResponseRedirect(reverse('index:index'))  # Следует переписать путь до админ панели
            return HttpResponseRedirect(reverse('index:register', args=(1,)))
        else:
            return HttpResponseRedirect(reverse('index:register', args=(0,)))
    except:
        raise Http404
