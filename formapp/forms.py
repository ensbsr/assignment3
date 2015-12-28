from django import forms
from formapp.models import Student
from formapp.models import Course

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(label='e-mail address')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        num_words = len(first_name.split())
        if num_words > 3:
            raise forms.ValidationError("Not a valid name!")
        return first_name

class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(label='Your e-mail address')
    office_details = forms.CharField(max_length=140)
    phone = forms.CharField(max_length=30)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        num_words = len(first_name.split())
        if num_words > 3:
            raise forms.ValidationError("Not a valid name!")
        return first_name

    def clean_office_details(self):
        office_details = self.cleaned_data['office_details']
        num_words = len(office_details.split())
        if num_words > 3:
            raise forms.ValidationError("Not a valid detail!")
        return office_details

class CourseForm(forms.Form):
    #student = forms.ModelMultipleChoiceField(StudentForm)
    course_name = forms.CharField(max_length=30)
    course_code = forms.CharField(max_length=3)
    course_classroom = forms.CharField(max_length=30)
    course_time = forms.CharField(max_length=30)

class enrollForm(forms.Form):
	course = forms.ModelChoiceField(queryset=Course.objects, empty_label=None)
	student = forms.ModelChoiceField(queryset=Student.objects, empty_label=None)