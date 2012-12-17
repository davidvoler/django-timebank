from django.conf.urls.defaults import *

urlpatterns = patterns('timebank.accounts.views',
    (r'^$', 'my_account'),
)
