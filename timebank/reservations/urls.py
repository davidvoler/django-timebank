from django.conf.urls.defaults import *

urlpatterns = patterns('timebank.reservations.views',
    #(r'^s/(?P<s_id>\w+)/$', 'service'),
    (r'^appointment/(?P<a_id>\w+)/$', 'appointment'),
    (r'^reserve/(?P<s_id>\w+)/$', 'reserve'),
    (r'^respond/(?P<r_id>\w+)/(?P<action>\w+)/$', 'respond'),
    (r'^appointments/$', 'appointments'),
    (r'^reservations/$', 'reservations'),
    
    
)
