from django.urls import path
from . import views

urlpatterns = [
    path("add-subject/", views.add_subject, name="add_subject"),
    path("subjects/", views.view_subjects, name="view_subjects"),
    path("delete-subject/<int:id>/", views.delete_subject, name="delete_subject"),
    path("add-exam/", views.add_exam, name="add_exam"),
    path("delete-exam/<int:id>/", views.delete_exam, name="delete_exam"),
    path("timetable/", views.view_timetable, name="view_timetable"),
    path("assign-subject/", views.assign_subject, name="assign_subject"),
    path("timetable/<int:student_id>/", views.student_timetable, name="student_timetable"),

]
