from django.db import models
from django.contrib import auth
from django.contrib.auth import login
from registration.signals import *
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	website = models.URLField("Website", blank=True)
	institution = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50)

	def __unicode__(self):
		return self.user.username

def createUserProfile(sender, user, request, **kwargs):
	UserProfile.objects.get_or_create(user=user)

user_registered.connect(createUserProfile)

def get_absolute_url(self):
	return ('profiles_profile_detail', (), {'username': self.user.username })
	get_absolute_url = models.permalink(get_absolute_url)
