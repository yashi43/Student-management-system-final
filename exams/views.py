from django.shortcuts import render, redirect
from .models import Subject, ExamSchedule, StudentSubject
from students.models import Student

def add_subject(request):
    subjects = Subject.objects.all()   # fetch all existing subjects

    if request.method == "POST":
        code = request.POST["code"]
        name = request.POST["name"]

        Subject.objects.create(code=code, name=name)

        # Instead of redirecting, reload the same page with updated list
        subjects = Subject.objects.all()
        return render(request, "exams/add_subject.html", {"subjects": subjects})

    return render(request, "exams/add_subject.html", {"subjects": subjects})


def view_subjects(request):
    subjects = Subject.objects.all()
    return render(request, "exams/view_subjects.html", {"subjects": subjects})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, ExamSchedule

def add_exam(request):
    subjects = Subject.objects.all()
    exams = ExamSchedule.objects.all()

    if request.method == "POST":
        subject_id = request.POST["subject"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        room = request.POST["room"]

        subject = Subject.objects.get(id=subject_id)

        ExamSchedule.objects.create(
            subject=subject,
            date=date,
            start_time=start_time,
            end_time=end_time,
            room=room
        )

        return redirect("add_exam")

    return render(request, "exams/add_exam.html", {"subjects": subjects, "exams": exams})



from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamSchedule
  

def delete_exam(request, id):
    exam = get_object_or_404(ExamSchedule, id=id)
    exam.delete()
    return redirect("add_exam")




def view_timetable(request):
    exams = ExamSchedule.objects.all().order_by("date")
    return render(request, "exams/view_timetable.html", {"exams": exams})

def assign_subject(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    assigned = StudentSubject.objects.select_related("student", "subject")

    if request.method == "POST":
        student_id = request.POST["student"]
        subject_id = request.POST["subject"]

        StudentSubject.objects.create(
            student_id=student_id,
            subject_id=subject_id
        )
        assigned = StudentSubject.objects.select_related("student", "subject")

    return render(request, "exams/assign_subject.html", {
        "students": students,
        "subjects": subjects,
        "assigned": assigned
    })

from .models import StudentSubject

def delete_assignment(request, id):
    record = StudentSubject.objects.get(id=id)
    record.delete()
    return redirect("assign_subject")



from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject

def delete_subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect("view_subjects")


def student_timetable(request, student_id):
    assigned = StudentSubject.objects.filter(student_id=student_id)
    subjects = [a.subject for a in assigned]
    exams = ExamSchedule.objects.filter(subject__in=subjects).order_by("date")

    return render(request, "exams/student_timetable.html", {
        "exams": exams,
        "student": Student.objects.get(id=student_id)
    })
