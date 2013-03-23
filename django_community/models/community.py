"""
A community model for handling sites with multiple communities

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Community(models.Model):
    owner = models.ForeignKey(User)
    name  = models.CharField(_('Name'),max_length=255 )
    overview = models.TextField(_('Overview'))
    url_suffix = models.CharField(_('URL Suffix'),max_length=50,null=True,blank=True )
    site = models.ForeignKey(Site,null=True,blank=True)
    location = models.CharField(_('URL Suffix'),max_length=50,null=True,blank=True )
    language = models.CharField(_('Language'),max_length=15,null=True,blank=True )
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    class Meta:
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        app_label = "django_community"
        