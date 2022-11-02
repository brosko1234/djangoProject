from django.conf import settings
from django.conf.urls.static import static


from . import views
from django.urls import path, include

from .views import index, register

urlpatterns = [
    path('', index, name='home'),
    path('Register', register, name='Register')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
