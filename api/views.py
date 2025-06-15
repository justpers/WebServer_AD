from rest_framework import generics
from pybo.models import Answer, Question
from .serializers import AnswerSerializer
from rest_framework.pagination import PageNumberPagination

class AnswerPagination(PageNumberPagination):
    page_size = 5  # 한 페이지에 답변 5개
    page_size_query_param = 'page_size'

class AnswerListAPI(generics.ListAPIView):
    serializer_class = AnswerSerializer
    pagination_class = AnswerPagination

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Answer.objects.filter(question__id=question_id).order_by('-create_date')