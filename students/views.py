from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def add_student(request):
    students = Student.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        roll_number = request.POST["roll_number"]
        email = request.POST["email"]

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            email=email
        )
        return redirect("add_student")

    return render(request, "students/add_student.html", {"students": students})


def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/update_student.html", {"form": form, "student": student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")
