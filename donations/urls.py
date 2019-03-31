from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', donations, name = 'donations'),
    url(r'^in_progres/$', in_progres, name = 'in_progres')
    ]
    


