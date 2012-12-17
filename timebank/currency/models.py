from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Currency(models.Model):
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    name = models.CharField(max_length=255)
    decription = models.TextField(null=True,blank=True)
    rate = models.FloatField(default=0,null=True,blank=True)
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"
    def __unicode__(self):
        return self.name
