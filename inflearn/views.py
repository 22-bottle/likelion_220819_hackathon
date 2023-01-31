from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lecture
from .forms import CourseForm, LectureForm

# Create your views here.

def home(request):
    return render(request, "index.html")

def courses(request):
    courses = Course.objects.filter().order_by('-date')
    lectures = Lecture.objects.filter().order_by('date')
    return render(request, 'courses.html', {'courses':courses, 'lectures':lectures})

def open_course(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.teacher = request.user
            unfinished.save()
        return redirect('home')
    else:
        form = CourseForm()
        return render(request, 'open_course.html', {'form':form})

def course_detail(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    lectures = Lecture.objects.filter().order_by('date')

    return render(request, 'course_detail.html', {'course_detail':course_detail, 'lectures':lectures})

def open_lecture(request, course_id):
    if request.method == 'POST' or request.method == 'FILES':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.teacher = request.user
            unfinished.course = get_object_or_404(Course, pk=course_id)
            unfinished.save()
        return redirect('course_detail', course_id)
    else:
        form = LectureForm()
        return render(request, 'open_lecture.html', {'form':form})

def lecture_detail(request, course_id, lecture_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)

    return render(request, 'lecture_detail.html', {'lecture_detail':lecture_detail})