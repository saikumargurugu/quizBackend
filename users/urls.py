from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView


urlpatterns = [
    path('signup', RegistrationView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('change-password', ChangePasswordView.as_view()),
]