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

from timebank.transactions.models import Transaction
from timebank.services.models import Service, Reservation

def search(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 

def add_service(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 
def edit_service(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 
def delete_service(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 

#list services
def services(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 
    
#admin
def admin_services(request):
    return render_to_response('timebank/services/add_service.html',
                              {},
            context_instance =  RequestContext(request)) 
