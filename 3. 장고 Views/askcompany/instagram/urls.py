from django.urls import path, re_path, register_converter
from . import views
from .converters import DayConverter, MonthConverter, YearConverter

app_name = 'instagram'

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name ='post_detail'),
    #re_path(r'(?p<pk>\d)/$', views.post_detail), #위 문장과 동일한 기능
    #path('archives/<year:year>/', views.archives_year),
    #re_path(r'archives/(?P<year>20\d{2})', views.archives_year),
    
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>', views.post_archive_year, name='post_archive_year'),
    #path('archive/<year:year>/<month:month>', views.post_archive_month, name='post_archive_month'),
]