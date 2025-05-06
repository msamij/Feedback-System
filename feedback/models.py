from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=15)

    def __str__(self):
        return self.choice_text


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""$Student name: {self.name}, Student phone no: ${self.phone_no}, 
    		Student course name: ${self.course_name}, Student teacher: ${self.teacher_name}"""


class StudentFeedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
