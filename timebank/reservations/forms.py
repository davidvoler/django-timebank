from django.forms import ModelForm

from timebank.reservations.models import Appointment,Reservation

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date',
                  'comments')
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('rdate',
                  'message',
                  'location'
                  )
        
class RespondForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('rdate',
                  'message',
                  'location',
                  'action'
                  )