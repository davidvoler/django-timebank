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

#from timebank.transactions.models import Transaction
from timebank.services.models import Service,Theme
from timebank.services.forms import ServiceForm

#list services
def my(request):
    services=Service.objects.filter(owner=request.user)
    return render_to_response('services/my_services.html',
                              {'services':services},
            context_instance =  RequestContext(request)) 
def services(request,theme):
    
    services=Service.objects.filter(published=True,auth=1).exclude(owner = request.user)
    if theme!='0':
        services=services.filter(theme=theme)
        sel_theme=Theme.objects.get(pk=theme)
        
        service_theme=sel_theme.name
    else:
        service_theme='All'
    
    return render_to_response('services/services.html',
                              {'services':services,
                               'theme':theme,
                               'service_theme':service_theme},
            context_instance =  RequestContext(request)) 
def service(request,s_id):
    """
    Allow users to reserve directly in this page
    if request.user.is_active:
        prof=request.user.get_profile()
    if prof.has_credit()
    form=ReservForm()
    //can be moved to the html (if form)
    Else ac_message=_('You are out of credit - you can not make new reservatons')
    
    See users reservations and apointments on this service
    ....
    
    Enable adding service to favorite
    
    
    """
    service=Service.objects.get(pk=s_id)    
    return render_to_response('services/service.html',
                              {'service':service},
            context_instance =  RequestContext(request)) 

@login_required
def add(request):
    service=Service(owner=request.user)
    form=ServiceForm(data=request.POST or None, instance=service)
    if form.is_valid():
        service=form.save()
        return HttpResponseRedirect('/services/s/%d/'%service.pk)
    return render_to_response('services/add.html',
                              {'form':form,},
            context_instance =  RequestContext(request)) 
@login_required
def edit(request,s_id):
    service=get_object_or_404(Service,pk=s_id,owner=request.user)
    form=ServiceForm(data=request.POST or None, instance=service)
    if form.is_valid():
        service=form.save()
        service.auth=2
        service.save()
        return HttpResponseRedirect('/services/s/%d/'%service.pk)
    return render_to_response('services/edit.html',
                              {'form':form,
                               'service':service},
            context_instance =  RequestContext(request)) 

def search(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 


def delete_service(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 

    
#admin
def admin_services(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 
