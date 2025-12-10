from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:pk>/', views.task_update, name='task-update'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
    path('toggle/<int:pk>/', views.task_toggle_complete, name='task-toggle'),
]