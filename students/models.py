from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
