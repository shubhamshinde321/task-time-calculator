from django.urls import path
from . import views

app_name = 'user_form'
urlpatterns = [
    path('task/', views.user_form, name="task_form"),
    path('task_list/', views.task_Data, name="task_list"),
]
