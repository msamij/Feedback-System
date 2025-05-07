from django.shortcuts import render, redirect
from .models import Question, Student, StudentFeedback


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        course_name = request.POST.get('course_name')
        teacher_name = request.POST.get('teacher_name')

        student = Student.objects.create(
            name=name,
            phone_no=phone_no,
            course_name=course_name,
            teacher_name=teacher_name
        )
        return redirect('feedback_form', student_id=student.id)

    return render(request, 'feedback/register.html')


def feedback_form(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        for key, value in request.POST.items():
            if key.startswith('q'):
                question_id = key[1:]
                choice_value = value
                question = Question.objects.get(id=question_id)

                StudentFeedback.objects.create(
                    student=student,
                    question=question,
                    choice=choice_value
                )

        return render(request, 'feedback/thankyou.html')
    questions = Question.objects.all()
    return render(request, 'feedback/feedback_form.html', {'questions': questions})
