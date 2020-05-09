from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:admin_login>/', views.index, name='index'),
    path('<str:admin_login>/<int:course_id>/', views.course, name='course'),
    path('<str:admin_login>/<int:course_id>/<int:topic_id>/', views.topic_edit, name='topic_edit'),
    # path('<str:admin_login>/<int:course_id>/<int:topic_id>/', views.topic_edit, name='topic_edit'),
]
