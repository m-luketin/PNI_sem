from django.shortcuts import render, redirect
from .models import AppUser, Course, AppUserCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

@login_required
def home(request):
    context = {
        'title': "Home",
        'content': AppUser.objects.all(),
    }
    return render(request, 'application/home.html', context)

@login_required
def course(request, course):
    context = {
        'course': Course.objects.filter(ime=course).first()
    }
    return render(request, 'application/course.html', context)

@login_required
def courseEdit(request, course):

    course = Course.objects.filter(ime=course).first()
    data={"ime": course.ime, "kod": course.kod, "program": course.program, "bodovi": course.bodovi, "sem_redovni": course.sem_redovni, "sem_izvanredni": course.sem_izvanredni, "izborni": course.izborni}

    if request.method == 'POST':
        form = courseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'course uspješno promijenjen!')
            return redirect('courses')
    else:
        form = courseForm(initial=data)
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'application/courseEdit.html', context)
       
@login_required
def studentEdit(request, appUser):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(email=appUser).first(),
        'content' : Course.objects.all()
    }
    appUser = AppUser.objects.filter(email=appUser).first()
    return render(request, 'application/studentEdit.html', content)

@login_required
def upisniList(request, appUser):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(email=appUser).first(),
        'content' : Course.objects.all()
    }
    appUser = AppUser.objects.filter(email=appUser).first()
    return render(request, 'application/upisniList.html', content)

def add(request, pk, cpk):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(id=pk).first(),
        'content' : Course.objects.all(),
        'fail': 0
    }
    student = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)
    if (cpk==49):
        oop = AppUserCourse.objects.filter(student_id=pk,course_id=20).first()
        if ( oop is None or oop.status != 'passed'):
            content = {
                'AppUserCourse' : AppUserCourse.objects.all(),
                'appUser' : AppUser.objects.filter(id=pk).first(),
                'content' : Course.objects.all(),
                'fail': 1
            }
            return render(request, 'application/studentEdit.html', content)

    email=student.email
    appUserCourse = AppUserCourse(student=student, course=course, status='enrolled')
    try:
        appUserCourse.save()
    except:
        return render(request, 'application/studentEdit.html', content)

    return render(request, 'application/studentEdit.html', content)

def remove(request, pk, cpk):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(id=pk).first(),
        'content' : Course.objects.all()
    }
    student = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)
    email=student.email
    try:
        AppUserCourse.objects.filter(student=student, course=course).delete()
    except:
        return render(request, 'application/studentEdit.html', content)

    return render(request, 'application/studentEdit.html', content)

def passed(request, pk, cpk):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(id=pk).first(),
        'content' : Course.objects.all()
    }
    student = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)
    email=student.email
    appUserCourse = AppUserCourse.objects.get(student=student, course=course)
    appUserCourse.status='passed'
    try:
        appUserCourse.save()
    except:
        return render(request, 'application/studentEdit.html', content)

    return render(request, 'application/studentEdit.html', content)


@login_required
def students(request):
    content = {
        'title': "Studenti",
        'content': AppUser.objects.all()
    }
    return render(request, 'application/students.html', content)

@login_required
def courses(request):
    content = {
        'title': "Course",
        'content': Course.objects.all()
    }
    return render(request, 'application/courses.html', content)


@login_required
def failedEnrollment():
    pass