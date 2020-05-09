from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from apps.index.models import Admin
from apps.admin_panel.models import Course, Topic


def index(request, admin_login=None):
    if admin_login is None:
        return HttpResponseRedirect(reverse('index:index'))
    else:
        courses_list = Course.objects.filter(admin=(Admin.objects.get(login=admin_login)))
        return render(request, 'admin_panel/index.html', {'courses_list': courses_list, 'admin_login': admin_login})


def edit(request, admin_login, course_id):
    topics_list = Topic.objects.filter(course=(Course.objects.get(id=course_id)))
    return render(request, 'admin_panel/course_inner.html', {'course_id': course_id, 'admin_login': admin_login,
                                                             'topics_list': topics_list})

