from django.conf.urls import url
from subdomains.tests.views import view


urlpatterns = [
    url(regex=r'^$', view=view, name='home'),
    url(regex=r'^example/$', view=view, name='example'),
]
