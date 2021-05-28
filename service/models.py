
from django.db import models

# Create our models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey






class Category(MPTTModel):
    STATUS = (
        ('Male','Erkek'),
        ('Female', 'Kadın'),
        ('Both', 'İkiside'),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_ate = models.DateTimeField(auto_now=True)

    class MPTTMeta:

        order_insertion_by = ['title']

    def __str__(self):
     full_path = [self.title]
     k = self.parent
     while k is not None:
        full_path.append(k.title)
        k = k.parent
     return ' -> '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'



class Service(models.Model):
        STATUS = (
            ('Male', 'Erkek'),
            ('Female', 'Kadın'),
            ('Both', 'İkiside'),
        )

        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        title = models.CharField(max_length=30)
        keyword = models.CharField(max_length=255)
        description = models.CharField(max_length=255)
        image = models.ImageField(blank=True, upload_to='images/')
        price = models.FloatField()
        status = models.CharField(max_length=10, choices=STATUS)
        slug = models.SlugField(blank=True,max_length=150)
        detail = RichTextUploadingField()
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        def __str__(self):
          return self.title

        def image_tag(self):
            if self.image:
                return mark_safe(f'<img src="{self.image.url}" height="50"/>')
            else:
                return ""




class Images(models.Model):
        service = models.ForeignKey(Service, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        image = models.ImageField(blank=True, upload_to='images/')





        def __str__(self):
          return self.title









