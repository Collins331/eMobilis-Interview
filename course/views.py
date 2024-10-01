from django.shortcuts import render

from course.models import Course


# Create your views here.
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'course/list_courses.html', {'courses': courses})

def update_course(request, pk):
    book = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=book)
    return render(request, 'course/update_course.html', {'form': form})