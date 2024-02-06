from django.urls import path
from .views import UserRegistrationView, home


urlpatterns = [
    path('', home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
