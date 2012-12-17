from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from timebank.reservations import Appointment
import datetime

#remiders to send
class Notification(models.Model):
    user=models.ForeignKey(User)
    active_from=models.DateTimeField(auto_now_add=True)
    active_until=models.DateTimeField(auto_now_add=True)
    ntype=models.CharField(max_length=100,null=True,blank=True,choices=(
                                                            ('reservation',_('reservation')),
                                                            ('appointment',_('appointment')),
                                                            ('balance',_('balance')),
                                                            ))
    subject=models.CharField(max_length=255,null=True,blank=True)
    short_message=models.CharField(max_length=255,null=True,blank=True)
    long_message_message=models.CharField(max_length=255,null=True,blank=True)
    sms_reminder_sent=models.BooleanField()
    email_reminder_sent=models.BooleanField()

class ReminderLog(models.Model):
    date_sent=models.DateTimeField(auto_now_add=True)
    r_type=models.CharField(max_length=10,default='email',null=True,blank=True)
    r_count=models.IntegerField(default=0,null=True,blank=True)
    @staticmethod
    def send_email(email,subject,message):
        pass
    @staticmethod
    def send_email_reminder():
        today=datetime.datetime.utcnow()-datetime.timedelta(days=1)
        ap=Appointment.objects.filter(email_reminder=True,
                                      email_reminder_sent=False,
                                      a_date__gte=today)
        count_sent=0
        for a in ap:
            #send reminder to provider
            ReminderLog.send_email(a.service.reciever.email, a.get_subject(), a.get_e_message())
            #send reminder to provider
            ReminderLog.send_email(a.reciever.email, a.get_subject(), a.get_e_message())
            a.email_reminder_sent=True
            a.save()
            count_sent+=2
        rl=ReminderLog(r_type='email',r_count=count_sent)
        rl.save()
    @staticmethod
    def send_sms(number,message):
        """
        #TODO:
        Add user profile with phone number for user that want to get reminders
        For SMS you may use one of the SMS packages from here:
        http://www.djangopackages.com/grids/g/sms/
        """         
        pass
    @staticmethod
    def send_sms_reminder():
        last_2_hours=datetime.datetime.utcnow()-datetime.timedelta(hours=2)
        ap=Appointment.objects.filter(sms_reminder=True,
                                      sms_reminder_sent=False,
                                      a_date__gte=last_2_hours)
        count_sent=0
        for a in ap:
            #send reminder to provider
            ReminderLog.send_sms(a.service.owner.get_profile().phone, a.get_subject(), a.get_sms_message())
            #send reminder to provider
            ReminderLog.send_sms(a.reciever.get_profile().phone, a.get_sms_message())
            a.sms_reminder_sent=True
            a.save()
            count_sent+=2
        rl=ReminderLog(r_type='sms',r_count=count_sent)
        rl.save()