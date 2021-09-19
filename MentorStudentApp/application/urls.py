from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('students/', views.students, name="students"),
    path('courses/', views.courses, name="courses"),
    path('course/<course>/', views.course, name="course"),
    path('courseEdit/<course>/', views.courseEdit, name="courseEdit"),
    path('studentEdit/<appUser>/', views.studentEdit, name="studentEdit"),
    path('add/<int:pk>/<int:cpk>/', views.add, name="add"),
    path('remove/<int:pk>/<int:cpk>/', views.remove, name="remove"),
    path('passed/<int:pk>/<int:cpk>/', views.passed, name="passed"),
]