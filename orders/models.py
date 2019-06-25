from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique instances

# Create your models here.
class Salad(models.Model):
    """Model contains all of the  dinner salads"""
    name = models.CharField(max_length=50, help_text='Enter a salad')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('salad_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class SaladInstance(models.Model):
    """Model representing a specific copy of a salad """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this salad')
    salad = models.ForeignKey('Salad', on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.salad.title})'

class Pasta(models.Model):
    """Model contains all of the pastas"""
    name = models.CharField(max_length=50, help_text='Enter a salad')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['price']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('pasta_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

#TODO Add instance before setting up orders
#TODO for Currency
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('formatted_amount', ...other fields...,)
#
#     def formatted_amount(self, obj):
#         # obj is the Model instance
#
#         # If your locale is properly set, try also:
#         # locale.currency(obj.amount, grouping=True)
#         return '%.2f EUR' % obj.amount
