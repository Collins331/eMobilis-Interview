from django.shortcuts import render, redirect

from course.models import Course
from .forms import CourseForm


# Create your views here.
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'course/list_courses.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'course/create_course.html', {'form': form})

def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/update_course.html', {'form': form})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course/course_detail.html', {'course': course})


def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'books/delete_course.html', {'course': course})
