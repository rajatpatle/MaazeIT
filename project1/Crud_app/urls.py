from django.urls import path
from . import views

urlpatterns = [
    path('av/', views.addEmp, name='add_url'),
    path('sv/', views.showEmp, name='show_url'),
    path('uv/<int:pk>/', views.updateEmp, name='update_url'),
    path('dv/<int:pk>/', views.deleteEmp, name='delete_url')
]