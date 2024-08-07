from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('result', views.analyse, name='result'),
    path('dev/', views.dev, name = 'dev')
]
