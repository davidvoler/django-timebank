from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from timebank.services.models import Service
from timebank.reservations.models import Appointment
#Penalty Period
PENALTY_HALF=4
PENALTY_FULL=1

class Account(models.Model):
    user = models.ForeignKey(User)
    balance=models.FloatField(default=0)     
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"
    def get_notification(self,user):
        pass
    
"""
Records any action that might affect balance
"""
class Transaction(models.Model):
    user= models.ForeignKey(User)
    appointment=models.ForeignKey(Appointment)
    t_date  = models.DateTimeField(default=None,null=True,blank=True)
    amount = models.IntegerField(default=0,null=True,blank=True)
    payed_to = models.ForeignKey(User, related_name='payed_to')
    payed_by = models.ForeignKey(User, related_name='payed_by')
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    status=models.IntegerField(default=0,null=True,blank=True)
    closed = models.BooleanField()
    canceled= models.BooleanField()
    title=models.CharField(max_length=255,null=True,blank=True)
    comments=models.TextField(null=True,blank=True)
    action=models.IntegerField(null=True,blank=True)
    #class Meta:
        #abstract= True
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        #app_label = "services"
    def cancel(self):
        #reversing transaction 
        pass
    
class Transfer(models.Model):
    user=models.ForeignKey(User)
    transaction=models.ForeignKey(Transaction)
    balance=models.IntegerField(default=0,null=True,blank=True)
    amount=models.IntegerField(default=0,null=True,blank=True)
    created_date  = models.DateTimeField(auto_now_add=True,editable=False,default=None,null=True,blank=True)
    changed  = models.DateTimeField(auto_now=True,editable=False,default=None,null=True,blank=True)
    class Meta:
        ordering = ['-created_date']

"""
    @staticmethod
    def appointment_action(ap,action,user):
        try:
            tr=Transaction.objects.get(appointment=ap)
        except:
            tr=Transaction(appointment=ap)
        if action==10:
            tr.minutes=ap.length
            tr.payed_to=ap.service.owner
            tr.payed_by=ap.reciever
            pt_ac=Account.objects.get(user=tr.payed_to)
            pb_ac=Account.objects.get(user=tr.payed_by)
            pt_ac.balance+=tr.minutes
            pb_ac.balance-=tr.minutes
            tr.save()
            pt_ac.save()
            pb_ac.save()
            jr=Journal(transaction=tr,
                       created_by=user,
                       action=action,
                       payed_to=tr.payed_to,
                       payed_by=tr.payed_by
                       )
            jr.save()
            
            
        elif action==-4:#Cancel Service
            #TODO: if in no penalty period. 
            penalty_half=datetime.datetime.utcnow()-datetime.timedelta(days=PENALTY_HALF)
            penalty_full=datetime.datetime.utcnow()-datetime.timedelta(days=PENALTY_FULL)
            if ap.appointment_date>penalty_half:
                #clear the transaction- return all the money passed
                pass
            elif ap.appointment_date<penalty_full:
                #transaction is not change only mark it is a penalty
                #What do we do if one of the users did not show of
                pass
            else:
                #reverse earlier transaction, pass half of the penalty from the canceling user to the other user 
                pass
            if user==ap.reciever:
                pass
            elif user==ap.service.owner:
                pass
        elif action==-5:#Mutual Cancellation
            pt_ac=Account.objects.get(user=tr.payed_to)
            pb_ac=Account.objects.get(user=tr.payed_by)
            pt_ac.balance-=ap.length
            pb_ac.balance+=ap.length
            pt_ac.save()
            pb_ac.save()
            tr.payed_by=ap.service.owner
            tr.payed_to=ap.reciever
            tr.save()
            jr=Journal(transaction=tr,
                       created_by=user,
                       action=action,
                       payed_to=ap.reciever,
                       payed_by=ap.service.owner
                       )
            jr.save() 
            
            
            
        
                
        
        #TODO: Depending on the action set the transaction
        #Activate: pass time currency from provider to reciever
        #Cancel : depends on rules and who canceled    
        tr.save()
        
        #TODO: Change balance
        #TODO: This function should be a transaction from database point of view




class Journal(models.Model):
    transaction=models.ForeignKey(Transaction)
    action=models.IntegerField(default=0,null=True,blank=True)
    created_by = models.ForeignKey(User)
    minutes = models.IntegerField(default=0,null=True,blank=True)
    payed_by = models.ForeignKey(User,related_name='payed_by')
    payed_to = models.ForeignKey(User,related_name='payed_to')

""" 