from django.urls import path

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path('feedback/', views.feedback_form, name='feedback_form'),

]
