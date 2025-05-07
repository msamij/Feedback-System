from django.urls import path

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path('feedback/<int:student_id>/', views.feedback_form, name='feedback_form'),
]
