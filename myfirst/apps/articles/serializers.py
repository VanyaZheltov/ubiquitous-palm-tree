from rest_framework import serializers
from .models import Dialog
class DialogSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length = 100)
    answer = serializers.CharField(max_length = 100)
    class Meta:
        model = Dialog
        fields = ("question", "answer")
