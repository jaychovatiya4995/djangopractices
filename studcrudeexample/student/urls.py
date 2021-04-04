from django.urls import path
from . import views

urlpatterns = [
    path('show_book/', views.show_book),
    path('add_book/', views.add_book),
    path('edit_book/<int:id>', views.edit_book),
    path('update_book/<int:id>', views.update_book),
    path('delete_book/<int:id>', views.delete_book),

    path('show_stream', views.show_stream),
    path('add_stream/', views.add_stream),
    path('edit_stream/<int:id>', views.edit_stream),
    path('update_stream/<int:id>', views.update_stream),
    path('delete_stream/<int:id>', views.delete_stream),

    path('show_student/', views.show_student),
    path('add_student/', views.add_student),
    path('edit_student/<int:id>', views.edit_student),
    path('update_student/<int:id>', views.update_student),
    path('delete_student/<int:id>', views.delete_student),    

]