from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register-student/', views.register_student, name='register_student'),
    path('register-course/', views.register_course, name='register_course'),
    path('student-list/<int:course_id>/', views.student_list, name='student_list'),
    path('projects_register/', views.register_project, name='register_project'),
    path('project_student_list/<int:project_id>/', views.project_student_list, name='project_student_list'),
    #path('student_detail/<int:stu_id>/', views.student_detail, name='student_detail'),

    path('students/', views.StudentListView.as_view(), name='student_list_all'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    
]