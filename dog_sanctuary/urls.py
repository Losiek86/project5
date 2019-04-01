"""dog_sanctuary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as urls_home
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from products import urls as urls_products 
from articles import urls as urls_articles
from pupils import urls as urls_pupils
from donations import urls as urls_donations
from volo import urls as urls_volo
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^products/', include(urls_products)),
    url(r'^article/', include(urls_articles)),
    url(r'^pupils/', include(urls_pupils)),
    url(r'^donations/', include(urls_donations)),
    url(r'^volo/', include(urls_volo)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
