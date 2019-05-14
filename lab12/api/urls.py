from django.urls import path
from api import views
urlpatterns = [
    path('api/task_lists/', views.all_task_list),
    path('api/task_lists/<int:pk>/', views.task_detail),
    path('api/task_lists/<int:pk>/tasks/', views.id_task_list)
]

