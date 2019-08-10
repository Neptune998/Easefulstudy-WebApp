from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),

]