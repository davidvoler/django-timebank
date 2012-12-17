from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.translation import ugettext as _
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

import datetime
from timebank.transactions.models import Transaction
from timebank.reservations.models import Appointment, Reservation
from timebank.services.models import Service
from timebank.reservations.forms import ReservationForm,RespondForm

@login_required
def appointment(request,a_id):
    ap=Appointment.objects.get(pk=a_id)
    return render_to_response('reservations/appointment.html',
                              {'ap':ap,
                               'cancel':True,
                               'accept':True,
                               'reject':True,
                               'reschedule':True
                               },
            context_instance =  RequestContext(request)) 

@login_required
def respond(request,r_id,action):
    reserv=Reservation.objects.get(pk=r_id)
    response=reserv.create_response(request.user)
    response.action=int(action)
    form=RespondForm(data=request.POST or None, instance=response)
    if form.is_valid():
        response=form.save()
        response.response=reserv
        response.set_appointment(request.user)
        return HttpResponseRedirect('/reservations/appointment/%d'%reserv.appointment.id)
    return render_to_response('reservations/respond.html',
                              {'form':form,
                               'response':response,
                               'action':action,},
            context_instance =  RequestContext(request)) 


@login_required
def appointments(request):
    """
    Show user's appointments
    """
    aps=Appointment.objects.filter((Q(service__owner=request.user)|
                                     Q(reciever=request.user))&
                                   Q(status=10)&
                                   Q(appointment_date__gte=datetime.datetime.now()))
    return render_to_response('reservations/appointments.html',
                              {'aps':aps},
            context_instance =  RequestContext(request)) 

@login_required
def reservations(request):
    """
    Show user's open reservations
    """
    my_res=Appointment.objects.filter(reciever=request.user,status=1)
    other_res=Appointment.objects.filter(service__owner=request.user,status=1)
    return render_to_response('reservations/reservations.html',
                              {'my_res':my_res,
                               'other_res':other_res},
            context_instance =  RequestContext(request)) 


@login_required
def reserve(request,s_id):
    service=Service.objects.get(pk=s_id)
    reserv=Reservation(initiator=request.user,
                       target=service.owner)
    form=ReservationForm(data=request.POST or None, instance=reserv)
    if form.is_valid():
        reserv=form.save()
        reserv.set_appointment(request.user,service)
        return HttpResponseRedirect('/reservations/appointments/')
    return render_to_response('reservations/reserve.html',
                              {'form':form,
                               'reserv':reserv},
            context_instance =  RequestContext(request)) 

@login_required
def reserve_response(request,r_id):
    """
    Reaction to reservation:
    options are:
    Accept
    Reject
    Change time/location
    Leave it in current status only send a message
    
    Simple Solution Create a form in a messagebox 
    Use a real form with post 
    
    """
    action=request.GET.get('action','')
    if action=='accept':
        pass
    elif action=='reject':
        pass
    elif action=='reschedule':
        pass
    reserv=Reservation.objects.get(pk=r_id)
    response=Reservation(appointment=reserv.appointment,
                         initiator=request.user,
                         target=reserv.initiator,
                         response_to=reserv)
    
    form=ReservationResponseForm(data=request.POST or None, instance=response)
    if form.is_valid():
        response=form.save()
        response.set_appointment(request.user)
        return HttpResponseRedirect('/reservations/status/%d/'%reserv.pk)
    return render_to_response('reservations/reserve_response.html',
                              {'form':form,
                               'reserv':reserv},
            context_instance =  RequestContext(request)) 



@login_required
def reject(request,r_id):
    pass
@login_required
def reschedule(request,r_id):
    pass
@login_required
def my_reservations(request):
    return render_to_response('timebank/reservations/accept_reject.html',
                              {},
            context_instance =  RequestContext(request)) 
@login_required
def my_requsts(request):
    return render_to_response('timebank/reservations/accept_reject.html',
                              {},
            context_instance =  RequestContext(request)) 
@login_required
def my_appointments(request):
    return render_to_response('timebank/reservations/accept_reject.html',
                              {},
            context_instance =  RequestContext(request)) 
