from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
]