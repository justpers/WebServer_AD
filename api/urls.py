from django.urls import path
from .views import AnswerListAPI

urlpatterns = [
    path('questions/<int:question_id>/answers/', AnswerListAPI.as_view(), name='answer-list-api'),
]