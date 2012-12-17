from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from timebank.currency.models import Currency

class Theme(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Service(models.Model):
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    owner = models.ForeignKey(User)
    published = models.BooleanField()
    auth = models.IntegerField(default=0,choices=((-1,_('Inappropriate')),
                                                  (0,_('New')),
                                                  (1,_('Authorized')),
                                                  (2,_('Edited')),
                                                  ))
    theme=models.ForeignKey(Theme)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    minutes = models.IntegerField(default=60,null=True,blank=True)
    min_minutes = models.IntegerField(default=30,null=True,blank=True)
    max_minutes = models.IntegerField(default=90,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    currency = models.ForeignKey(Currency,null=True,blank=True)
    cost = models.IntegerField(default=1,null=True,blank=True)
    def __unicode__(self):
        return "%s:%s"%(self.theme, self.title)
    
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"
