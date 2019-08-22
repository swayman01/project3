from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique instances




class Regularpizza(models.Model):
    """Model contains all of the pizza"""
    name = models.CharField(max_length=50, help_text='')
    toppings = models.ManyToManyField('Topping', blank=True, related_name='regularpizza')
    smallprice = models.DecimalField(max_digits=5, decimal_places=2)
    largeprice = models.DecimalField(max_digits=5, decimal_places=2)
    numtoppings = models.IntegerField(default = 0)

    class Meta:
        ordering = ['smallprice']

    def get_absolute_url(self):
        """Returns the url to access a particular salad instance."""
        return reverse('regularpizza_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Salad(models.Model):
    """Model contains all of the dinner salads"""
    name = models.CharField(max_length=50, help_text='')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['price']

    def get_absolute_url(self):
        """Returns the url to access a particular salad instance."""
        return reverse('salad_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# class SaladInstance(models.Model):
#     """Model representing a specific copy of a salad """
#     # TODO: Do we need this model? See what happens with Pasta
#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this salad')
#     salad = models.ForeignKey('Salad', on_delete=models.SET_NULL, null=True)
#
#     # class Meta:
#     #     ordering = ['name']
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.id} ({self.salad.title})'


class Pasta(models.Model):
    """Model contains all of the pastas"""
    name = models.CharField(max_length=50, help_text='')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['price']

    def get_absolute_url(self):
        """Returns the url to access a particular pasta instance."""
        return reverse('pasta_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Topping(models.Model):
    """Model contains all of the toppings"""
    name = models.CharField(max_length=50, help_text='')
    popularity = models.DecimalField(max_digits=5, decimal_places=2)
    # popularity is for menu order

    class Meta:
        ordering = ['popularity']

    def get_absolute_url(self):
        """Returns the url to access a particular pasta instance."""
        return reverse('topping_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Order(models.Model):
    """Model contains all of the orders"""
    orderowner = models.IntegerField(default = 0)
    #0: guest
    orderdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    # auto_now_add automatically set the field to now when the object is first created.
    """
    A date and time, represented in Python by a datetime.datetime instance.
    Takes the same extra arguments as DateField.
    The default form widget for this field is a single TextInput.
    The admin uses two separate TextInput widgets with JavaScript shortcuts.
"""
    foodname = models.CharField(max_length=50, help_text='')
    #TODO: Strategize toppings
    foodprice = models.DecimalField(max_digits=5, decimal_places=2)
    foodrating = models.IntegerField(default = 0)
    # 0: no rating, -1: thumbs down, -2: thumbs up
    popularity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-orderdate']
    # It is highlly unlikely that two orders will be submitted at the exact same time
    # so on need to sort by orderowner
    # It seems to me it is probably more efficient to sort by thumbs on
    # small database for customers viewing orders and the sort by rating
    # across the database by a manager will be infrequent

    def get_absolute_url(self):
        """Returns the url to access a particular pasta instance."""
        return reverse('topping_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


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
