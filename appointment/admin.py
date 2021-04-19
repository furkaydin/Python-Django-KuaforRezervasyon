from django.contrib import admin

# Register your models here.
from appointment.models import Category, Service


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'status']
    list_filter = ['status', ]

class ServiceAdmin(admin.ModelAdmin):
        list_display = ['category', 'price', 'title', 'status']
        list_filter = ['status', 'category',]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)

