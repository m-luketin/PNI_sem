from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('students/', views.students, name="students"),
    path('mentors/', views.mentors, name="mentors"),
    path('courses/', views.courses, name="courses"),
    path('course/<course>/', views.course, name="course"),
    path('courseEdit/<course>/', views.courseEdit, name="courseEdit"),
    path('addCourse/', views.addCourse, name="addCourse"),
    path('studentEdit/<appUser>/', views.studentEdit, name="studentEdit"),
    path('addStudent/', views.addStudent, name="addStudent"),
    path('editStudentAttributes/<appUser>', views.editStudentAttributes, name="editStudentAttributes"),
    path('mentorEdit/<appUser>/', views.mentorEdit, name="mentorEdit"),
    path('add/<int:pk>/<int:cpk>/', views.add, name="add"),
    path('remove/<int:pk>/<int:cpk>/', views.remove, name="remove"),
    path('passed/<int:pk>/<int:cpk>/', views.passed, name="passed"),
    path('mentorCourses/<mentor>/', views.mentorCourses, name="mentorCourses"),
    path('courseStudents/<course>/', views.courseStudents, name="courseStudents"),    
    path('courseStudents/<course>/<int:pk>/<int:cpk>/<action>', views.enrollStudent, name="enrollStudent"),
    path('mentorAdd/<int:pk>/<int:cpk>/', views.mentorAdd, name="mentorAdd"),
    path('mentorRemove/<int:pk>/<int:cpk>/', views.mentorRemove, name="mentorRemove"),
    path('mentorPersonalCourses/', views.mentorPersonalCourses, name="mentorPersonalCourses"),
]