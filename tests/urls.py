from django.urls import path
from .views import SingleQuestionaryView,MultipleQuestionaryView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('single_questions', SingleQuestionaryView.as_view()),
    path('multi_questions', MultipleQuestionaryView.as_view()),
]