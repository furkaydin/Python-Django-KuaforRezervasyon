import admin_thumbnails
from django.contrib import admin

from home.models import Setting, ContactFormMessage, UserProfile


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    list_filter = ['status']

@admin_thumbnails.thumbnail('image')
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','image_thumbnail']



admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)

