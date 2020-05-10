from django.urls import path
from . import views

app_name = 'lk'
urlpatterns = [
    path('<str:user_login>', views.index, name="index"),
    path('<str:user_login>/view_courses', views.view_courses, name="view_courses"),
]
