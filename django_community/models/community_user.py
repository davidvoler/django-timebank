from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django_community.models.community import Community
"""
A single user in the database
"""
class CommunityUser(User):
    location = models.CharField(_('URL Suffix'),max_length=50,null=True,blank=True )
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    class Meta:
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        app_label = "django_community"
        