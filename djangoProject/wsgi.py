<<<<<<< HEAD
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

=======
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

>>>>>>> 28db349d9fc26775f91308aec53ddc052260599d
application = get_wsgi_application()