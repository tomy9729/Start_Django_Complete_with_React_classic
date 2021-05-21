from django.urls import path, re_path
from . import views

app_name = 'blog1'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]