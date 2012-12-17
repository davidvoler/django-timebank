from django.core.management.base import BaseCommand, CommandError
from timebank.reminder.models import ReminderLog

class Command(BaseCommand):
    help = 'send news latter about new solutions'
    #TODO: See how to use help and args and options
    def handle(self, *args, **options):
        res=ReminderLog.send_sms_reminder()
        #self.stdout.write(res)

