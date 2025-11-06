from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        roll_number = request.POST.get('roll_number')
        address = request.POST.get('address')
        Student.objects.create(
            name=name,
            email=email,
            course=course,
            roll_number=roll_number,
            address=address
        )
        return redirect('home')
    return render(request, 'add.html')

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')
