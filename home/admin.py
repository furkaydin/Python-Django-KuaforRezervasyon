import admin_thumbnails
from django.contrib import admin

from home.models import Setting, ContactFormMessage, UserProfile, FAQ


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    list_filter = ['status']

@admin_thumbnails.thumbnail('image')
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','image_thumbnail']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','status']
    list_filter = ['status']




admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FAQ, FAQAdmin)

