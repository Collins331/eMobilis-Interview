from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'course/create_course.html', {'form': form})

def update_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/update_course.html', {'form': form})

def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course/course_detail.html', {'course': course})


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    return render(request, 'course/delete_course.html', {'course': course})