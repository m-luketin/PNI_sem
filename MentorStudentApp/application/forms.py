from django import forms
from application.models import Course, AppUser, AppUserCourse
from django.contrib.auth.forms import UserCreationForm

class CourseForm(forms.ModelForm):
    name = forms.CharField()
    code = forms.CharField()
    program = forms.CharField()
    points = forms.IntegerField()
    regularSemester = forms.IntegerField()
    irregularSemester = forms.IntegerField()
    optional = forms.CheckboxInput()
    
    class Meta:
        model= Course
        fields=["name", "code", "program", "points", "regularSemester", "irregularSemester", "optional"]

