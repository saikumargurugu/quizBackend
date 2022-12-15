from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from .serializers import QuestionariesSerializer, TeseSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from .models import Questionaries,Answers, Test, SINGLE, MULTIPLE,TestScoresScores
import json
# Create your views here.


class SingleQuestionaryView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes=[]
    serializer_class = QuestionariesSerializer

    def get_queryset(self):
        print('===================')
        return Questionaries.objects.filter(questionaries_parent_id=int(self.request.data['question_parent_id']))

    def post(self, request, *args, **kwargs):
        list= self.list(request, *args, **kwargs)
        if 'user' not in request.data or 'questions' not in request.data:
            return Response({'msg': 'Mssing user or quetions'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TeseSerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save()
            obj.questions_count = len(list.data)
            obj.save()
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
        return Questionaries.objects.filter(questionaries_parent_id=int(self.request.data['question_parent_id']))

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

    def post(self, request):
        passed = 0
        failed = 0
        testParent = Test.objects.get(exam_id=request.data['exam_id'])
        if testParent.completed_at:
            return Response({'msg':'Test has been alredy submitted'}, status=status.HTTP_400_BAD_REQUEST)
        submited_answers = request.data['answers']
        print(len(submited_answers),testParent.questions_count)
        if len(submited_answers)==testParent.questions_count:
            if testParent.questions.questions_type== SINGLE:
                for k,v in submited_answers.items():
                    question = Questionaries.objects.get(id=int(k))
                    question.options.all().values_list('id')
                    print(question.options.all().values_list('id',flat=True),v)
                    if v not in question.options.all().values_list('id',flat=True):
                        return Response({"msg":"incorrect options, please select answer from given option "}, 
                        status=status.HTTP_400_BAD_REQUEST)
                    try:
                        print(question.answers.all().get(id=v))
                        question.answers.all().get(id=v)
                        passed = passed +1
                    except Exception as e :
                        print(e)
                        failed = failed +1
            if testParent.questions.questions_type== MULTIPLE:
                submited_answers = request.data['answers']
                for k,v in submited_answers.items():
                    question = Questionaries.objects.get(id=int(k))
                    for ans in v:
                        if ans not in question.options.all().values_list('id'):
                            return Response({"msg":"incorrect options, please select answer from given option "}, 
                            status=status.HTTP_400_BAD_REQUEST)
                    correct_ids=question.answers.all().values_list('id')
                    if correct_ids.sort() == v.sort():
                        passed = passed +1
                    else:
                        failed = failed +1
            newScore = TestScoresScores()
            newScore.score = passed
            newScore.user_id = request.data['user']
            newScore.test = testParent
            newScore.save()
            return Response({"msg":"your  answers are " + str(passed) + " and your wrong answers are " + str(failed)},
            status= status.HTTP_200_OK
            )
        else:
            return Response({"msg":"incomplete answers, please attempt all answers"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg":"oops something went wront"}, status=status.HTTP_400_BAD_REQUEST)