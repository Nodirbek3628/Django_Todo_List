from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('add/',views.add_task, name='add')
]