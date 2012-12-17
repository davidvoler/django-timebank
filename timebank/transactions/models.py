from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import *
from timebank.reservations.models import Reservation

class Transaction(models.Model):
    reservation=models.ForeignKey(Reservation)
    t_date  = models.DateTimeField(default=None,null=True,blank=True)
    minutes = models.IntegerField(default=60,null=True,blank=True)
    reciever = models.ForeignKey(User)
    provider = models.ForeignKey(User, related_name='provider')
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    closed = models.BooleanField()
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"

