from . import views
from django.urls import path

urlpatterns=[
    path('',views.home, name='home'),
    path('new_search', views.new_search, name='new_search')
]
