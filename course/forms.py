from django.forms import  forms
from course.models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = '__all__'