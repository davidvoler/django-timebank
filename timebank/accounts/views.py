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
from timebank.accounts.models import Account,Transaction,Transfer

def my_account(request):
    account=Account.objects.get(user=request.user)
    transfers=Transfer.objects.filter(user=request.user)
    return render_to_response('accounts/my_account.html',
                              {'account':account,
                               'transfers':transfers},
            context_instance =  RequestContext(request)) 
