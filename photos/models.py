from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class ReadMore(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    text = models.TextField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Read More"
        verbose_name_plural = "Read More DB"