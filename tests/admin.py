from django.contrib import admin
from .models import Questionaries, Options, Test, TestScoresScores, QuestionariesParent


admin.site.register(Questionaries)
admin.site.register(Options)
admin.site.register(TestScoresScores)
admin.site.register(QuestionariesParent)
admin.site.register(Test)

