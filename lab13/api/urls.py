from django.urls import path
from api import views

#urlpatterns = [
    #path('api/task_lists/', views.all_task_list),
    #path('api/task_lists/<int:pk>/', views.task_detail),
   # path('api/task_lists/<int:pk>/tasks/', views.id_task_list)
#]

urlpatterns = [
     path('users/', views.UserList.as_view()),
     path('api/task_lists/', views.All_Task_List.as_view()),
     path('api/task_lists/<int:pk>/', views.Task_Detail.as_view()),
     path('login/', views.login),
     path('logout/', views.logout),
    #path('api/task_lists/<int:pk>/tasks/', views.id_task_list)

]

