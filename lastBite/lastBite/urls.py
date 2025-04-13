from django.template.base import kwarg_re
from django.urls import path
from shopApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)