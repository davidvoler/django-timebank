from django.forms import ModelForm

from timebank.services.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = (
                  'title',
                  'theme',
                  'description',
                  'location',
                  'min_minutes',
                  'max_minutes' ,                 
                  'published')
