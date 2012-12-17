from django.conf import settings
from django.contrib.auth.models import User
from timebank import get_notifications
def timebank_notifications(request):
    notifications=get_notifications(request.user)
    return {"notifications":notifications}

            