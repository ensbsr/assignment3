from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.template import  RequestContext
from formapp.models import Student
from formapp.models import Teacher
from formapp.forms import StudentForm
from formapp.forms import TeacherForm
from formapp.models import Course
from formapp.forms import CourseForm
from formapp.forms import enrollForm

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all_student/')
    else:
        form = StudentForm(initial={"first_name": "Your Name Goes Here!"})
    return render_to_response('addstudent.html', {'form': form},
                        RequestContext(request))

def all_student(request):
    return render_to_response('tablestudent.html',
    {'student_list': Student.objects.all()})

def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"],
                        office_details=form.cleaned_data["office_details"],
                        phone = form.cleaned_data["phone"])
            a.save()
            return HttpResponseRedirect('/all_teacher/')
    else:
        form = TeacherForm(initial={"first_name": "Your Name Goes Here!"})
    return render_to_response('addteacher.html', {'form': form},
                        RequestContext(request))

def all_teacher(request):
    return render_to_response('tableteacher.html',
    {'teacher_list': Teacher.objects.all()})

def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            a = Course(course_name=form.cleaned_data["course_name"],
                       course_code=form.cleaned_data["course_code"],
                       course_classroom=form.cleaned_data["course_classroom"],
                       course_time=form.cleaned_data["course_time"],)
            a.save()
            return HttpResponseRedirect('/all_course/')
    else:
        form = CourseForm(initial={"course_name": "Course Name Goes Here!"})
    return render_to_response('addcourse.html', {'form': form},
                        RequestContext(request))

def all_course(request):
    return render_to_response('coursetable.html',
    {'course_list': Course.objects.all()})


def enroll(request):
	form = enrollForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			course_obj = form.cleaned_data['course']
			student_obj = form.cleaned_data['student']
			a = Student.objects.get(id=student_obj.id)
			b = Course.objects.get(id=course_obj.id)
			a.enrolled_courses.add(a)
			b.enrolled_students.add(b)


	return render_to_response('enroll.html', {'form': form}, RequestContext(request))

