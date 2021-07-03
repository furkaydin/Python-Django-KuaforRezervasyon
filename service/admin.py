import admin_thumbnails
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from service.models import Category, Service, Images, Comment, Barber


class ServiceImageInline(admin.TabularInline):
    model = Images
    extra = 5

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'status','image_thumbnail']
    list_filter = ['status', ]

class BarberAdmin(admin.ModelAdmin):

    list_display = ['name']

@admin_thumbnails.thumbnail('image')
class ServiceAdmin(admin.ModelAdmin):
        list_display = ['category', 'price','title','status','image_thumbnail']
        list_filter = ['status', 'category',]
        inlines = [ServiceImageInline]


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','service','image_thumbnail']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_service_count', 'related_service_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Service,
                'category',
                'service_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Service,
                 'category',
                 'service_count',
                 cumulative=False)
        return qs

    def related_service_count(self, instance):
        return instance.service_count
    related_service_count.short_description = 'Related services (for this specific category)'

    def related_service_cumulative_count(self, instance):
        return instance.service_cumulative_count
    related_service_cumulative_count.short_description = 'Related services (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','service','user','status',]
    list_filter = ['status']








admin.site.register(Category,CategoryAdmin2)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Barber,BarberAdmin)









