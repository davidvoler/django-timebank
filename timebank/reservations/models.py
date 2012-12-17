from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from timebank.services.models import Service


class Appointment(models.Model):
    service = models.ForeignKey(Service)
    reciever = models.ForeignKey(User)    
    responder = models.ForeignKey(User,related_name='responder',null=True,blank=True)    
    appointment_date  = models.DateTimeField(default=None,null=True,blank=True)
    length  = models.IntegerField(default=60,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    changed= models.DateTimeField(auto_now=True,null=True,blank=True,editable=False)
    comments=models.TextField(null=True,blank=True)
    status=models.IntegerField(default=1,null=True,blank=True,
                               choices=((1,_('Tentative')),
                                        (0,_('Rejected')),
                                        (10,_('Active')),
                                        (-4,_('Canceled')),
                                        ))
    class Meta:
        ordering =['-appointment_date']
    def activate(self):
        self.status=10
        """
        TODO: Add transaction
        """
        pass
    def cancel(self):
        self.status=-1
        """
        TODO: Add cancelation actions (transaction)
        """
    def reserve_action(self,action,user):
        from timebank.accounts import pass_currency 
        if user==self.reciever:
            self.responder=self.service.owner
        else:
            self.responder=self.reciever
        if action==10:
            self.status=10
            self.responder=None
            pass_currency(action,
                          self.length,
                          user,
                          self.reciever,
                          self.service.owner,
                          self,
                          '')
            self.save()
        elif action==1:
            self.status=0
            self.responder=None
            self.save()
                        


class Reservation(models.Model):
    appointment = models.ForeignKey(Appointment,null=True,blank=True)
    response_to = models.ForeignKey('self',null=True,blank=True)
    initiator = models.ForeignKey(User)    
    target = models.ForeignKey(User,related_name="target")    
    rdate  = models.DateTimeField(default=None,null=True,blank=True)
    minutes = models.IntegerField(default=60,null=True,blank=True)
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    viewed=models.BooleanField()
    response=models.BooleanField()
    
    status=models.IntegerField(default=0,null=True,blank=True,
                               choices=((0,_('Open')),
                                        (1,_('Closed')),
                                        ))
    action=models.IntegerField(default=0,null=True,blank=True,
                               choices=((0,_('Message')),
                                        (1,_('Reject')),
                                        (2,_('Change Date or Location')),
                                        (10,_('Accept')),
                                        (11,_('Cancel')),
                                        (12,_('Accept Cancel')),
                                        (13,_('Mutual Cancellation')),
                                        (14,_('Accept Mutual Cancellation')),
                                        ))
    class Meta:
        ordering =['-created_date']
        
    def respond(self):
        """
        Action that need to be taken on reservation respond
        """
        pass
    def set_appointment_old(self,user):
        self.appointment.reserve_action(self.action,user)
          
    def set_appointment(self,user,service=None):
        if self.response:
            self.appointment=self.response.appointment
            self.location=self.response.location
            self.rdate=self.response.rdate
            if self.action in [10,1,2]:
                self.response.status=1
        else:
            ap=Appointment(service=service,
                          reciever=user,
                          responder=service.owner,
                          appointment_date=self.rdate
                          )
            ap.save()
            self.appointment=ap
        self.save()
        self.appointment.reserve_action(self.action,user)
        #TODO: Generate notification
    def create_response(self,user):
        response=Reservation(appointment=self.appointment,
                     initiator=user,
                     target=self.initiator,
                     response_to=self)
        return response