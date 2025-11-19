from django.urls import path
from . import views

urlpatterns = [
    path("add_student/", views.add_student, name="add_student"),
    path("list/", views.student_list, name="student_list"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
]
