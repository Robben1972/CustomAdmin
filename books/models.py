from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"

class Book(models.Model):
    title = models.CharField(blank=False, max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, verbose_name='Amount')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books', null=True)
    published_date = models.DateField(blank=False)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title