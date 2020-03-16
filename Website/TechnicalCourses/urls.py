from django.urls import path
from . import views

app_name = 'TechnicalCourses'

urlpatterns = [
    path('<int:course_id>/',views.detail, name='detail'),
    path('', views.Courses, name = 'home-page'),
    path('<int:course_id>/yourchoice/',views.your_choice, name = 'your-choice')
]