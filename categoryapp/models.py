from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='category_covers/')

    def __str__(self):
        return self.name
