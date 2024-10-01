from  django.urls import path
from . import views


urlpatterns = [
    path('', views.list_courses, name='courses'),
    path('create/', views.create_course, name='create_course'),
    path('<int:id>/', views.course_detail, name='course'),
    path('<int:id>/update', views.update_course, name='update'),
    path('<int:id>/delete', views.delete_course, name='delete'),
]