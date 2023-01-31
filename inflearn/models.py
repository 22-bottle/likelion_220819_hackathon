from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lecture(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.TextField()
    url = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.lecture