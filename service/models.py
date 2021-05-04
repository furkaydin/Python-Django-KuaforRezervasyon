
from django.db import models

# Create our models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
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
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_ate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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
        detail = models.TextField()
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        def __str__(self):
          return self.title

        def image_tag(self):
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        image_tag.short_description = 'Image'









class Images(models.Model):
        service = models.ForeignKey(Service, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        image = models.ImageField(blank=True, upload_to='images/')
        def __str__(self):
          return self.title






