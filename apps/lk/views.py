from django.shortcuts import render
from django.http import Http404
from apps.index.models import User, Admin
from apps.admin_panel.models import Specialization, StaticGraph


def index(request, user_login):
    try:
        user = User.objects.get(login=user_login)
    except:
        raise Http404
    return render(request, 'lk/index.html', {'user_instance': user, 'list_companies': Admin.objects.all(),
                                             'list_spec': Specialization.objects.all(),
                                             'ex_image0': StaticGraph.objects.all()[0],
                                             'ex_image1': StaticGraph.objects.all()[1]})
