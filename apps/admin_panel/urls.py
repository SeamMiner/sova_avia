from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:admin_login>/', views.index, name='index'),
    path('<str:admin_login>/<int:course_id>/', views.edit, name='edit'),
    # path('<str:admin_login>/<int:course_id>/<int:topic_id>/', views.edit, name='edit'),
]
