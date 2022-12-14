from rest_framework import serializers
from .models import Questionaries, Answers, Options, Test
from django.utils import timezone
import uuid

class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = '__all__'

class QuestionariesSerializer(serializers.ModelSerializer):
    options= serializers.SerializerMethodField()
    class Meta:
        model = Questionaries
        exclude = ['answers']

    def get_options(self,obj):
        return OptionsSerializer(obj.options.all(), many=True).data


class TeseSerializer(serializers.ModelSerializer):
    exam_id = serializers.SerializerMethodField()
    class Meta:
        model = Test
        fields = '__all__'

    def save(self):
        test = Test()
        test.user = self.validated_data['user']
        test.questions=self.validated_data['questions']
        test.created_at = timezone.now()
        test.exam_id = uuid.uuid4()
        test.save()
        return test
    
    def get_exam_id(self,obj):
        print(obj)