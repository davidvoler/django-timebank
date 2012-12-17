from django.conf.urls.defaults import *

urlpatterns = patterns('timebank.services.views',
    (r'^s/(?P<s_id>\w+)/$', 'service'),
    (r'^add/$', 'add'),
    (r'^my/$', 'my'),
    (r'^edit/(?P<s_id>\w+)/$', 'edit'),
    (r'^(?P<theme>\w+)/$', 'services'),
)
