from rest_framework import serializers
from pybo.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'content', 'create_date', 'modify_date', 'author_username']
