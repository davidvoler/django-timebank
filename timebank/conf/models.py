from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

"""
TODO:Add setting for cancellation policy 
"""

class Conf(models.Model):
    max_minus  = models.FloatField()
    max_plus  = models.FloatField()
    allow_register  = models.BooleanField()
    review_service  = models.BooleanField()
    
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"

