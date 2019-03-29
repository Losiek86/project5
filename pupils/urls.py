from django.conf.urls import include, url
from .views import all_pupils, pupil

urlpatterns = [
    url(r'^show_all/$', all_pupils, name = 'pupils'),
    url(r'^(?P<pupil_id>\d+)/$', pupil, name = 'pupil'),
    ]