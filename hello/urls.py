from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)


urlpatterns=[
    path("get_students/", views.get_students),       #api endpoint to get students and store students
    path("", views.front, name='front'),  #randers template directly to the front end
    path("fetchdata/", views.fetchdata, name='fetchdata'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('api/', include(router.urls)) #router path to direct to student viewset which handles all CRUD operations
]