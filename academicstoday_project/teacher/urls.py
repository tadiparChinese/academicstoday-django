from django.urls import include, path
from . import views

# Import custom views.
from teacher.views import announcement
from teacher.views import syllabus
from teacher.views import policy
from teacher.views import lecture
from teacher.views import lecture_note
from teacher.views import assignment
from teacher.views import quiz
from teacher.views import exam
from teacher.views import overview
from teacher.views import discussion
from teacher.views import peer_review
from teacher.views import setting

app_name = 'teacher'

urlpatterns = [
    # Syllabus
    path('teacher/course/(\d+)/overview/', overview.overview_page),
    path('teacher/course/(\d+)/submit_course_for_review/',
         overview.submit_course_for_review),

    # Announcement
    path('teacher/course/(\d+)/', announcement.announcements_page),
    path('teacher/course/(\d+)/home/', announcement.announcements_page),
    path('teacher/course/(\d+)/announcement/', announcement.announcements_page),
    path('teacher/course/(\d+)/announcements_table/',
         announcement.announcements_table),
    path('teacher/course/(\d+)/announcement_modal/',
         announcement.announcement_modal),
    path('teacher/course/(\d+)/save_announcement/',
         announcement.save_announcement),
    path('teacher/course/(\d+)/delete_announcement/',
         announcement.delete_announcement),

    # Syllabus
    path('teacher/course/(\d+)/syllabus/', syllabus.syllabus_page),
    path('teacher/course/(\d+)/syllabus_modal/', syllabus.syllabus_modal),
    path('teacher/course/(\d+)/save_syllabus/', syllabus.save_syllabus),
    path('teacher/course/(\d+)/delete_syllabus/', syllabus.delete_syllabus),

    # Policy
    path('teacher/course/(\d+)/policy/', policy.policy_page),
    path('teacher/course/(\d+)/policy_modal/', policy.policy_modal),
    path('teacher/course/(\d+)/save_policy/', policy.save_policy),
    path('teacher/course/(\d+)/delete_policy/', policy.delete_policy),

    # Lecture
    path('teacher/course/(\d+)/lectures/', lecture.lectures_page),
    path('teacher/course/(\d+)/lectures_table/', lecture.lectures_table),
    path('teacher/course/(\d+)/lecture_modal/', lecture.lecture_modal),
    path('teacher/course/(\d+)/save_lecture/', lecture.save_lecture),
    path('teacher/course/(\d+)/delete_lecture/', lecture.delete_lecture),

    # Lecture Note(s)
    path('teacher/course/(\d+)/lecture/(\d+)/notes/',
         lecture_note.lecture_notes_page),
    path('teacher/course/(\d+)/lecture/(\d+)/lecture_notes_table/',
         lecture_note.lecture_notes_table),
    path('teacher/course/(\d+)/lecture/(\d+)/lecture_note_modal/',
         lecture_note.lecture_note_modal),
    path('teacher/course/(\d+)/lecture/(\d+)/save_lecture_note/',
         lecture_note.save_lecture_note),
    path('teacher/course/(\d+)/lecture/(\d+)/delete_lecture_note/',
         lecture_note.delete_lecture_note),

    # Assignment(s)
    path('teacher/course/(\d+)/assignments/', assignment.assignments_page),
    path('teacher/course/(\d+)/assignments_table/', assignment.assignments_table),
    path('teacher/course/(\d+)/assignment_modal/', assignment.assignment_modal),
    path('teacher/course/(\d+)/save_assignment/', assignment.save_assignment),
    path('teacher/course/(\d+)/delete_assignment/', assignment.delete_assignment),

    # Assignment
    path('teacher/course/(\d+)/assignment/(\d+)/', assignment.assignment_page),
    path('teacher/course/(\d+)/assignment/(\d+)/questions_table/',
         assignment.questions_table),
    path('teacher/course/(\d+)/assignment/(\d+)/question_type_modal/',
         assignment.question_type_modal),
    path('teacher/course/(\d+)/assignment/(\d+)/question_essay_modal/',
         assignment.question_essay_modal),
    path('teacher/course/(\d+)/assignment/(\d+)/question_multiple_choice_modal/',
         assignment.question_multiple_choice_modal),
    path('teacher/course/(\d+)/assignment/(\d+)/question_true_false_modal/',
         assignment.question_true_false_modal),
    path('teacher/course/(\d+)/assignment/(\d+)/question_response_modal/',
         assignment.question_response_modal),
    path('teacher/course/(\d+)/assignment/(\d+)/save_question/',
         assignment.save_question),
    path('teacher/course/(\d+)/assignment/(\d+)/delete_question/',
         assignment.delete_question),

    # Quiz(es)
    path('teacher/course/(\d+)/quizzes/', quiz.quizzes_page),
    path('teacher/course/(\d+)/quizzes_table/', quiz.quizzes_table),
    path('teacher/course/(\d+)/quiz_modal/', quiz.quiz_modal),
    path('teacher/course/(\d+)/save_quiz/', quiz.save_quiz),
    path('teacher/course/(\d+)/delete_quiz/', quiz.delete_quiz),

    # Quiz
    path('teacher/course/(\d+)/quiz/(\d+)/', quiz.quiz_page),
    path('teacher/course/(\d+)/quiz/(\d+)/questions_table/', quiz.questions_table),
    path('teacher/course/(\d+)/quiz/(\d+)/question_type_modal/',
         quiz.question_type_modal),
    path('teacher/course/(\d+)/quiz/(\d+)/question_true_false_modal/',
         quiz.question_true_false_modal),
    path('teacher/course/(\d+)/quiz/(\d+)/save_question/', quiz.save_question),
    path('teacher/course/(\d+)/quiz/(\d+)/delete_question/', quiz.delete_question),

    # Exam(s)
    path('teacher/course/(\d+)/exams/', exam.exams_page),
    path('teacher/course/(\d+)/exams_table/', exam.exams_table),
    path('teacher/course/(\d+)/exam_modal/', exam.exam_modal),
    path('teacher/course/(\d+)/save_exam/', exam.save_exam),
    path('teacher/course/(\d+)/delete_exam/', exam.delete_exam),

    # # Exam
    path('teacher/course/(\d+)/exam/(\d+)/', exam.exam_page),
    path('teacher/course/(\d+)/exam/(\d+)/questions_table/', exam.questions_table),
    path('teacher/course/(\d+)/exam/(\d+)/question_type_modal/',
         exam.question_type_modal),
    path('teacher/course/(\d+)/exam/(\d+)/question_multiple_choice_modal/',
         exam.question_multiple_choice_modal),
    path('teacher/course/(\d+)/exam/(\d+)/save_question/', exam.save_question),
    path('teacher/course/(\d+)/exam/(\d+)/delete_question/', exam.delete_question),

    # Discussion
    path('teacher/course/(\d+)/discussion/', discussion.discussion_page),
    path('teacher/course/(\d+)/discussions_table/', discussion.discussions_table),
    path('teacher/course/(\d+)/new_thread/', discussion.new_thread_modal),
    path('teacher/course/(\d+)/insert_thread/', discussion.insert_thread),
    path('teacher/course/(\d+)/delete_thread/', discussion.delete_thread),
    path('teacher/course/(\d+)/thread/(\d+)/', discussion.posts_page),
    path('teacher/course/(\d+)/thread/(\d+)/posts_table/', discussion.posts_table),
    path('teacher/course/(\d+)/thread/(\d+)/new_post/', discussion.new_post_modal),
    path('teacher/course/(\d+)/thread/(\d+)/insert_post/', discussion.insert_post),

    # Peer-Review
    path('teacher/course/(\d+)/peer_reviews/', peer_review.peer_reviews_page),
    path('teacher/course/(\d+)/peer_review/(\d+)/', peer_review.assignment_page),
    path('teacher/course/(\d+)/peer_review/(\d+)/peer_review_modal/',
         peer_review.peer_review_modal),
    path('teacher/course/(\d+)/peer_review/(\d+)/save_peer_review/',
         peer_review.save_peer_review),
    path('teacher/course/(\d+)/peer_review/(\d+)/delete_peer_review/',
         peer_review.delete_peer_review),
    path('teacher/course/(\d+)/peer_review/(\d+)/update_assignment_marks/',
         peer_review.update_assignment_marks),

    # Settings
    path('teacher/course/(\d+)/settings/', setting.settings_page),
    path('teacher/course/(\d+)/suspend_course/', setting.suspend_course),
]
