"""ms_iv_ua URL Configuration

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
from django.views import static
from home.views import index
from home import urls as urls_home
from accounts import urls as urls_accounts
from content import urls as urls_content
from issue import urls as urls_issue
from feature import urls as urls_feature
from payment import urls as urls_payment
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^home/', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^content/', include(urls_content)),
    url(r'^issue/', include(urls_issue)),
    url(r'^feature/', include(urls_feature)),
    url(r'^payment/', include(urls_payment)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
