from django.shortcuts import render
from .models import Category,Course

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{'categories':categories})

def courses(request):
    return render(request,'Courses.html')


def home_view(request):
    courses = Course.objects.all()
    return render(request, 'home.html',{'courses':courses})

