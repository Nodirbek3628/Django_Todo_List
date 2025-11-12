from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('',views.get_task_list_view, name='list'),
    path('add/',views.add_task_view, name='add')
]