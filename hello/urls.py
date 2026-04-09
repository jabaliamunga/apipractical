from django.urls import path
from . import views

urlpatterns=[
    path("get_students/", views.get_students),       #api endpoint to get students and store students
    path("", views.front, name='front'),  #randers template directly to the front end
    path("fetchdata/", views.fetchdata, name='fetchdata'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]