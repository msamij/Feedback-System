from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, Student


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        course_name = request.POST.get('course_name')
        teacher_name = request.POST.get('teacher_name')

        # student = Student.objects.create(
        #     name=name,
        #     phone_no=phone_no,
        #     course_name=course_name,
        #     teacher_name=teacher_name
        # )
        # return HttpResponse(f"Name: {name}, Phone: {phone_no}, Course: {course_name}, Teacher: {teacher_name}")
        return redirect('feedback_form')

    return render(request, 'feedback/register.html')


def feedback_form(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('q'):
                question_id = key[1:]
                choice_id = value
                print(
                    f'Question ID: {question_id}, Selected Choice ID: {choice_id}')
        return HttpResponse('Feedback submitted successfully!')

    questions = Question.objects.all()
    return render(request, 'feedback/feedback_form.html', {'questions': questions})
