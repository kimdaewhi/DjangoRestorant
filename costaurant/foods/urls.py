from django.contrib import admin
from django.urls import path
from foods import views

urlpatterns = [
    path('', views.index),
    # 동적 url 처리, food_detail에 파라미터로 넘겨줌
    path('<int:pk>/', views.food_detail)
]
