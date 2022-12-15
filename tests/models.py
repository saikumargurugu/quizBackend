from django.db import models
from users.models import User
# Create your models here.
import uuid

SINGLE = 'Single'
MULTIPLE = 'Multiple'

QUESTION_TYPES = (
    (SINGLE,'SINGLE'),
    (MULTIPLE,'MULTIPLE')
)

class Answers(models.Model):
    answers = models.CharField(max_length=500)
    def __str__(self):
        return self.answers

class Options(models.Model):
    option= models.CharField(max_length=500)
    def __str__(self):
        return self.option

class QuestionariesParent(models.Model):
    Name = models.CharField(max_length=500)
    questions_type = models.CharField(choices=QUESTION_TYPES,max_length=20, null= True)
    def __str__(self):
        return self.Name


class Questionaries(models.Model):
    question = models.CharField(max_length=500)
    options = models.ManyToManyField(Options, related_name='question_options')
    answers = models.ManyToManyField(Answers, related_name='question_answers')
    questionaries_parent= models.ForeignKey(QuestionariesParent,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class Test(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)
    completed_at= models.DateTimeField(blank=True, null=True)
    exam_id= models.UUIDField(
         default = uuid.uuid4,
         unique=True)
    questions = models.ForeignKey(QuestionariesParent, on_delete=models.SET_NULL, null= True)
    questions_count= models.IntegerField(default=0)
    def __str__(self):
        print(self.exam_id)
        return str(self.exam_id)

class TestScoresScores(models.Model):

    test= models.ForeignKey(Test, on_delete=models.SET_NULL, null= True)
    score=  models.FloatField(default=0.00)
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.test__exam_id + self.score