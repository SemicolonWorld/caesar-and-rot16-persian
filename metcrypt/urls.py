from django.urls import path
from . import views

app_name = 'metcrypt'

urlpatterns = [
    path('', views.caesar, name='home'),
    path('caesar/', views.caesar, name='caesar'),
    path('rot16/', views.rot16, name='rot16'),
    
]