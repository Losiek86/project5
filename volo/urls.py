from django.conf.urls import include, url
from .views import volo, check

urlpatterns = [
    url(r'^$', volo, name = 'volo'),
    url(r'^check/$', check, name = 'check'),
    ]