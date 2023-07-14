from django.conf.urls import url
from django.urls import path, include, re_path
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from home.api.views import *

urlpatterns = [
    path('encrypt/', Encrypt.as_view(), name='encrypt'),
    path('decrypt/', Decrypt.as_view(), name='decrypt'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 