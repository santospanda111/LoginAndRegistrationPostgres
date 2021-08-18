from django.urls import path
from UserRegistration import views as UserView

urlpatterns = [
    path('', UserView.Index.as_view(), name='homepage')
]