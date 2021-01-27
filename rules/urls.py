from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rules import views as rules_views

urlpatterns = [
    path('register/', rules_views.UserCreate.as_view()),
    path('auth/', obtain_auth_token, name='api_token_auth'),
]
