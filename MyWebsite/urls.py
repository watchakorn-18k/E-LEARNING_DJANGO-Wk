from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views.index ดึงฟังค์ชั่น views.py
    path('class_room/<int:id>', views.class_room, name='class_room'),
]
