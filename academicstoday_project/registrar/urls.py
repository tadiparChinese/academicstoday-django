from django.urls import include, path

from registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate

app_name = 'registrar'

urlpatterns = [
    # Courses
    path('courses/', courses.courses_page),
    path('enroll/', courses.enroll),

    # Enrollment(s)
    path('enrollment/', enrollment.enrollment_page),
    path('enrollment_table/', enrollment.enrollment_table),
    path('disenroll_modal/', enrollment.disenroll_modal),
    path('disenroll', enrollment.disenroll),

    # Teaching
    path('teaching/', teaching.teaching_page),
    path('refresh_teaching_table/', teaching.refresh_teaching_table),

    path('course_modal/', teaching.course_modal),
    path('save_course/', teaching.save_course),
    path('delete_course_modal/', teaching.delete_course_modal),
    path('course_delete/', teaching.course_delete),

    # Transcript
    path('transcript/', transcript.transcript_page),

    # Certificate(s)
    path('certificates/', certificate.certificates_page),
    path('certificates_table/', certificate.certificates_table),
    path('change_certificate_accessiblity/',
         certificate.change_certificate_accessiblity),
    #path('certificate/(\\d+)/', certificate.certificate_page),
    path('certificate/<int:credit_id>/', certificate.certificate_page),
    path('certificate_permalink_modal/',
         certificate.certificate_permalink_modal),
]
