from django.contrib import admin
from models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	search_fields=['user']
	list_display=('user','website', 'institution', 'country')
	ordering=('user',)

admin.site.register(UserProfile, UserProfileAdmin)
