from django.urls import path
from . import views

urlpatterns = [
    path('rv/', views.registerView, name='register_url'),
    path('lv/', views.loginView, name='log_url'),
    path('lgt/', views.logoutView, name='logout_url')
]