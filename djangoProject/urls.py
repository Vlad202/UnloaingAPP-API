<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

API_URL = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}account/'.format(API_URL), include('rules.urls')),
    path('{}clients/'.format(API_URL), include('clients.urls')),
]
=======
from django.contrib import admin
from django.urls import path, include

API_URL = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}account/'.format(API_URL), include('rules.urls')),
    path('{}clients/'.format(API_URL), include('clients.urls')),
]
>>>>>>> 28db349d9fc26775f91308aec53ddc052260599d
