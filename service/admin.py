import admin_thumbnails
from django.contrib import admin

# Register your models here.
from service.models import Category, Service, Images

class ServiceImageInline(admin.TabularInline):
    model = Images
    extra = 5

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'status','image_thumbnail']
    list_filter = ['status', ]


@admin_thumbnails.thumbnail('image')
class ServiceAdmin(admin.ModelAdmin):
        list_display = ['category', 'price','title','status','image_thumbnail',]
        list_filter = ['status', 'category',]
        inlines = [ServiceImageInline]

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','service','image_thumbnail']









admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Images,ImagesAdmin)








