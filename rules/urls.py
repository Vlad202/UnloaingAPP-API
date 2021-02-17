<<<<<<< HEAD
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rules import views as rules_views

urlpatterns = [
    path('register/', rules_views.UserCreate.as_view()),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('users/all/', rules_views.UsersList.as_view()),
    path('user/permission/', rules_views.UserPermission.as_view()),
]
=======
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rules import views as rules_views

urlpatterns = [
    path('register/', rules_views.UserCreate.as_view()),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('users/all/', rules_views.UsersList.as_view()),
    path('user/permission/', rules_views.UserPermission.as_view()),
]
>>>>>>> 28db349d9fc26775f91308aec53ddc052260599d
