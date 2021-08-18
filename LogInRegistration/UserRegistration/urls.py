from django.urls import path
from UserRegistration import views as UserView

urlpatterns = [
    path('', UserView.Index.as_view(), name='homepage'),
    path('/register', UserView.Register.as_view(), name='user_registration'),
    path('register/<int:pk>/', UserView.Register.as_view(), name='user_registration'),
    path('/login', UserView.LogIn.as_view(), name='user_login'),
    path('verify/<token>',UserView.VerifyEmail.as_view(),name='verify'),
    path('verify',UserView.VerifyEmail.as_view(),name='verify')
]