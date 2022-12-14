from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from .serializers import QuestionariesSerializer, TeseSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from .models import Questionaries,Answers, Options, SINGLE, MULTIPLE
import json
# Create your views here.


class SingleQuestionaryView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes=[]
    serializer_class = QuestionariesSerializer

    def get_queryset(self):
        return Questionaries.objects.filter(question_type=SINGLE)

    def post(self, request, *args, **kwargs):
        list= self.list(request, *args, **kwargs)
        if 'user' not in request.data or 'questions' not in request.data:
            return Response({'msg': 'Mssing user or quetions'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TeseSerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save()
            print(json.loads(json.dumps(list.data)))
            list.data= {
                "exam_id":obj.exam_id,
                "quetions": list.data
            }
        return list

class MultipleQuestionaryView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes=[]
    serializer_class = QuestionariesSerializer

    def get_queryset(self):
        return Questionaries.objects.filter(question_type=MULTIPLE)

    def get(self, request, *args, **kwargs):
        list =self.list(request, *args, **kwargs)
        if 'user' not in request.data or 'questions' not in request.data:
            return Response({'msg': 'Mssing user or quetions'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TeseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return list


class SubmitTest(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes=[]
    serializer_class = QuestionariesSerializer

    def get_queryset(self):
        return Questionaries.objects.filter(question_type=MULTIPLE)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

      