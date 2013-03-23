from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django_community.models.community_user import CommunityUser
from django_community.models.community import Community
"""
User information per community
"""

class CommunityProfile(User):
    user = models.ForeignKey(CommunityUser)
    community = models.ForeignKey(Community)
    #TODO Add some more information per community here
    class Meta:
        #ordering = ['weight','id']
        #db_table = 'mockup_content_item'
        app_label = "django_community"
        