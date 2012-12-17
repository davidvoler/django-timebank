from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from timebank.services.models import Service


class Appointment(models.Model):
    service = models.ForeignKey(Service)
    reciever = models.ForeignKey(User)    
    responder = models.ForeignKey(User,related_field='responder')    
    appointment_date  = models.DateTimeField(default=None,null=True,blank=True)
    length  = models.IntegerField(default=60,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    changed= models.DateTimeField(auto_now=True,null=True,blank=True,editable=False)
    comments=models.TextField(null=True,blank=True)
    status=models.IntegerField(defualt=0,null=True,blank=True,
                               choices=((0,_('Tentative')),
                                        (10,_('Active')),
                                        (2,_('Canceled')),
                                        ))
    class Meta:
        ordering =['-status','-appointment_date']
    def set_active(self):
        """
        """
        pass
    def cancel(self):
        """
        """
        pass


class Reservation(models.Model):
    appointment = models.ForeignKey(Appointment)
    reaction = models.ForeignKey('self',null=True,blank=True)
    initiator = models.ForeignKey(User)    
    target = models.ForeignKey(User,related_name="target")    
    rdate  = models.DateTimeField(default=None,null=True,blank=True)
    minutes = models.IntegerField(default=60,null=True,blank=True)
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    viewed=models.BooleanField()
    response=models.BooleanField()
    action=models.IntegerField(defualt=0,null=True,blank=True,
                               choices=((0,_('Reserve')),
                                        (1,_('Accept')),
                                        (2,_('Change Date')),
                                        (3,_('Change Location')),
                                        (4,_('Cancel')),
                                        (5,_('Mutual Cancellation')),
                                        (5,_('Message')),
                                        ))
    class Meta:
        ordering =['-created_date']
        
    def respond(self):
        """
        Action that need to be taken on reservation respond
        """
        pass
