from users.forms import AppUserForm
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
        'course': Course.objects.filter(name=course).first()
    }
    return render(request, 'application/course.html', context)

@login_required
def courseEdit(request, course):

    course = Course.objects.filter(name=course).first()
    data={"name": course.name, "code": course.code, "program": course.program, "points": course.points, "regularSemester": course.regularSemester, "irregularSemester": course.irregularSemester, "optional": course.optional}

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'course uspješno promijenjen!')
            return redirect('courses')
    else:
        form = CourseForm(initial=data)
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'application/courseEdit.html', context)

@login_required
def addCourse(request):

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'course uspješno dodan!')
            return redirect('courses')
    else:
        form = CourseForm()

    context = {
        'form': form,
        'course': course
    }

    return render(request, 'application/addCourse.html', context)

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
def addStudent(request):

    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'appUser uspješno dodan!')
            return redirect('students')
    else:
        form = AppUserForm()

    context = {
        'form': form
    }

    return render(request, 'application/addStudent.html', context)

@login_required
def mentorEdit(request, appUser):
    mentor = AppUser.objects.filter(email=appUser).first()
    data={"email": appUser}

    if request.method == 'POST':
        form = AppUserForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            messages.success(request, f'mentor uspješno promijenjen!')
            return redirect('mentors')
    else:
        form = AppUserForm(initial=data)
    context = {
        'form': form,
        'mentor': mentor
    }
    return render(request, 'application/mentorEdit.html', context)

@login_required
def editStudentAttributes(request, appUser):
    student = AppUser.objects.filter(email=appUser).first()
    data={"email": appUser}

    if request.method == 'POST':
        form = AppUserForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'student uspješno promijenjen!')
            return redirect('students')
    else:
        form = AppUserForm(initial=data)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'application/editStudentAttributes.html', context)

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
    appUser = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)

    if (AppUserCourse.objects.filter(appUser_id=appUser.id, course_id=course.id).exists()):
        return render(request, 'application/studentEdit.html', content)

    email=appUser.email
    appUserCourse = AppUserCourse(appUser=appUser, course=course)
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
    appUser = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)
    email=appUser.email
    try:
        AppUserCourse.objects.filter(appUser=appUser, course=course).delete()
    except:
        return render(request, 'application/studentEdit.html', content)

    return render(request, 'application/studentEdit.html', content)

def passed(request, pk, cpk):
    content ={
        'AppUserCourse' : AppUserCourse.objects.all(),
        'appUser' : AppUser.objects.filter(id=pk).first(),
        'content' : Course.objects.all()
    }
    appUser = AppUser.objects.get(id=pk)
    course = Course.objects.get(id=cpk)
    email=appUser.email
    appUserCourse = AppUserCourse.objects.get(appUser=appUser, course=course)
    appUserCourse.isPassed = True

    try:
        appUserCourse.save()
    except:
        return render(request, 'application/studentEdit.html', content)

    return render(request, 'application/studentEdit.html', content)


@login_required
def students(request):
    content = {
        'title': "Students",
        'content': AppUser.objects.all()
    }
    return render(request, 'application/students.html', content)


@login_required
def mentors(request):
    content = {
        'title': "Mentors",
        'content': AppUser.objects.all()
    }
    return render(request, 'application/mentors.html', content)

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