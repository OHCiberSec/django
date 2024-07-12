from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('detail/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('create/', views.lesson_create, name='lesson_create'),
    path('update/<int:pk>/', views.lesson_update, name='lesson_update'),
    path('delete/<int:pk>/', views.lesson_delete, name='lesson_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]