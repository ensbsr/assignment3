from django.conf.urls import patterns, include, url
from django.contrib import admin
from formapp.views import addstudent
#from form_app.views import search
from formapp.views import addstudent
from formapp.views import all_student
from formapp.views import all_teacher
from formapp.views import addteacher
from formapp.views import all_course
from formapp.views import addcourse
from formapp.views import enroll

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_student/', addstudent),
    url(r'^all_student/', all_student),
    url(r'^add_teacher/', addteacher),
    url(r'^all_teacher/', all_teacher),
    url(r'^add_course/', addcourse),
    url(r'^all_course/', all_course),
    url(r'^enroll/', enroll),


)
