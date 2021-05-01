from django.contrib import admin

# Register your models here.
from service.models import Category, Service, Images

class ServiceImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'status']
    list_filter = ['status', ]

class ServiceAdmin(admin.ModelAdmin):
        list_display = ['category', 'price', 'title', 'status']
        list_filter = ['status', 'category',]
        inlines = [ServiceImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','service','image']











admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Images,ImagesAdmin)








