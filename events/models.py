from django.db import models

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_name


class Events(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    thumbnail_image = models.ImageField(upload_to="", null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
