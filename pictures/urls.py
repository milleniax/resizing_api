from django.urls import path
from . import views

app_name = 'pictures'

urlpatterns = [
    path('', views.pictures, name='pictures'),
    path('rest/', views.ContentView.as_view(), name='rest'),
    path('task/<str:task_id>/', views.TaskView.as_view(), name = 'task'),
]
