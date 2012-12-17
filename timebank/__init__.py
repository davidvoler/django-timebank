from timebank.services.models import Theme,Service
from timebank.reservations.models import Reservation
from timebank.accounts.models import Account
from django.utils.translation import ugettext_lazy as _
import datetime
def get_notifications(user):
    if not user.is_active:
        return None
    #user balance
    nottifcation=[]
    try:
        ac=Account.objects.get(user=user)
    except:
        ac=Account(user=user)
        ac.save()
    
    b={'title':_('your balance is') +":%d"%ac.balance,
       'caption':_('balance')+":%d"%ac.balance,
       'link':'/accounts/'}
    nottifcation.append(b)
    #get apointments for today
    #reservs=Reservation.objects.filter(accepted=True,request_date)
    #get services that passed time and require confirmation
    return nottifcation
    
def list_themes():
    themes= Theme.objects.all()
    return themes
