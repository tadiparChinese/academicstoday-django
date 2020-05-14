#from django.urls import patterns, include, url
from django.urls import path, include

from . import views

# Import custom views.
from student.views import announcement
from student.views import syllabus
from student.views import policy
from student.views import lecture
from student.views import lecture_note
from student.views import assignment
from student.views import quiz
from student.views import exam
from student.views import discussion
from student.views import peer_review
from student.views import credit


app_name = 'student'

urlpatterns = [
    # Announcement
    path('course/(\\d+)/announcements/',
         announcement.announcements_page),

    # Syllabus
    path('course/(\\d+)/syllabus/', syllabus.syllabus_page),

    # Grades & Policy
    path('course/(\\d+)/policy/', policy.policy_page),

    # Lecture
    path('course/(\\d+)/lectures/', lecture.lectures_page),
    path('course/(\\d+)/lecture/', lecture.lecture),

    # Lecture Notes
    path('course/(\\d+)/lecture/(\\d+)/notes/',
         lecture_note.lecture_notes_page),
    path('course/(\\d+)/lecture/(\\d+)/view_lecture_note/',
         lecture_note.view_lecture_note),

    # Assignment(s)
    path('course/(\\d+)/assignments/',
         assignment.assignments_page),
    path('course/(\\d+)/assignments_table/',
         assignment.assignments_table),
    path('course/(\\d+)/delete_assignment/',
         assignment.delete_assignment),

    # Assignment
    path('course/(\\d+)/assignment/(\\d+)/',
         assignment.assignment_page),
    path('course/(\\d+)/assignment/(\\d+)/submit_assignment/',
         assignment.submit_assignment),
    path('course/(\\d+)/assignment/(\\d+)/submit_e_assignment_answer/',
         assignment.submit_e_assignment_answer),
    path('course/(\\d+)/assignment/(\\d+)/submit_mc_assignment_answer/',
         assignment.submit_mc_assignment_answer),
    path('course/(\\d+)/assignment/(\\d+)/submit_tf_assignment_answer/',
         assignment.submit_tf_assignment_answer),
    path('course/(\\d+)/assignment/(\\d+)/submit_r_assignment_answer/',
         assignment.submit_r_assignment_answer),

    # Quiz(zes)
    path('course/(\\d+)/quizzes/', quiz.quizzes_page),
    path('course/(\\d+)/quizzes_table/', quiz.quizzes_table),
    path('course/(\\d+)/quiz_delete/', quiz.delete_quiz),

    # Quiz
    path('course/(\\d+)/quiz/(\\d+)/', quiz.quiz_page),
    path('course/(\\d+)/quiz/(\\d+)/submit_quiz/',
         quiz.submit_quiz),
    path('course/(\\d+)/quiz/(\\d+)/submit_tf_quiz_answer/',
         quiz.submit_tf_assignment_answer),

    # Exam(s)
    path('course/(\\d+)/exams/', exam.exams_page),
    path('course/(\\d+)/exams_table/', exam.exams_table),
    path('course/(\\d+)/delete_exam/', exam.delete_exam),

    # Exam
    path('course/(\\d+)/exam/(\\d+)/', exam.exam_page),
    path('course/(\\d+)/exam/(\\d+)/submit_exam/',
         exam.submit_exam),
    path('course/(\\d+)/exam/(\\d+)/submit_mc_exam_answer/',
         exam.submit_mc_exam_answer),

    # Peer-Review
    path('course/(\\d+)/peer_reviews/',
         peer_review.peer_reviews_page),
    path('course/(\\d+)/peer_review/(\\d+)/',
         peer_review.assignment_page),
    path('course/(\\d+)/peer_review/(\\d+)/peer_review_modal/',
         peer_review.peer_review_modal),
    path('course/(\\d+)/peer_review/(\\d+)/save_peer_review/',
         peer_review.save_peer_review),
    path('course/(\\d+)/peer_review/(\\d+)/delete_peer_review/',
         peer_review.delete_peer_review),
    path('course/(\\d+)/peer_review/(\\d+)/update_assignment_marks/',
         peer_review.update_assignment_marks),

    # Discussion
    path('course/(\\d+)/discussion/',
         discussion.discussion_page),
    path('course/(\\d+)/threads_table/',
         discussion.threads_table),
    path('course/(\\d+)/new_thread/',
         discussion.new_thread_modal),
    path('course/(\\d+)/insert_thread/',
         discussion.insert_thread),
    path('course/(\\d+)/delete_thread/',
         discussion.delete_thread),
    path('course/(\\d+)/thread/(\\d+)/',
         discussion.thread_page),
    path('course/(\\d+)/thread/(\\d+)/posts_table/',
         discussion.posts_table),
    path('course/(\\d+)/thread/(\\d+)/new_post/',
         discussion.new_post_modal),
    path('course/(\\d+)/thread/(\\d+)/insert_post/',
         discussion.insert_post),

    # Credit
    path('course/(\\d+)/credit/', credit.credit_page),
    path('course/(\\d+)/submit_credit_application/',
         credit.submit_credit_application),
]
