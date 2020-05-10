from django.urls import path
from . import views

app_name = 'lk'
urlpatterns = [
    path('<str:user_login>', views.index, name="index")
]
