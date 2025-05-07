from django.contrib import admin
from .models import *


class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'question_text', 'choice', 'submitted_at')
    list_filter = ('student__course_name', 'student__teacher_name')
    search_fields = ('student__name', 'question__question_text', 'choice')

    def student_name(self, obj):
        return obj.student.name
    student_name.short_description = 'Student Name'

    def question_text(self, obj):
        return obj.question.question_text
    question_text.short_description = 'Question'

    def submitted_at(self, obj):
        return obj.student.submitted_at
    submitted_at.short_description = 'Submitted At'


admin.site.register(Question)
admin.site.register(Student)
admin.site.register(StudentFeedback, StudentFeedbackAdmin)
