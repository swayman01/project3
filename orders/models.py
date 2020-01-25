from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique instances

class Regularpizza(models.Model):
    """Model contains all of the Regulars pizzas"""
    name = models.CharField(max_length=50, help_text='')
    toppings = models.ManyToManyField('Topping', blank=True, related_name='regularpizza')
    smallprice = models.DecimalField(max_digits=5, decimal_places=2)
    largeprice = models.DecimalField(max_digits=5, decimal_places=2)
    numtoppings = models.IntegerField(default = 0)
    foodtype = models.CharField(max_length=50, help_text='')

    class Meta:
        ordering = ['smallprice']

    def get_absolute_url(self):
        """Returns the url to access a particular pizza instance."""
        return reverse('regularpizza_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Sicilianpizza(models.Model):
    """Model contains all of the Sicilian pizzas"""
    name = models.CharField(max_length=50, help_text='')
    toppings = models.ManyToManyField('Topping', blank=True, related_name='sicilianpizza')
    smallprice = models.DecimalField(max_digits=5, decimal_places=2)
    largeprice = models.DecimalField(max_digits=5, decimal_places=2)
    numtoppings = models.IntegerField(default = 0)
    foodtype = models.CharField(max_length=50, help_text='')

    class Meta:
        ordering = ['smallprice']

    def get_absolute_url(self):
        """Returns the url to access a particular pizza instance."""
        return reverse('sicilianpizza_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Sub(models.Model):
    """Model contains all of the Subs"""
    name = models.CharField(max_length=50, help_text='')
    smallprice = models.DecimalField(max_digits=5, decimal_places=2)
    largeprice = models.DecimalField(max_digits=5, decimal_places=2)
    #foodtype = models.CharField(max_length=50, help_text='')
    # display_order used to order items and identify add-ons. numbers to the
    # right of the decimal point indicate that it is an add-on
    display_order = models.DecimalField(max_digits=7, decimal_places=3)

    class Meta:
        ordering = ['display_order']

    def get_absolute_url(self):
        """Returns the url to access a particular sub instance."""
        return reverse('sub_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Dinnerplatter(models.Model):
    """Model contains all of the Dinner Platters"""
    name = models.CharField(max_length=50, help_text='')
    smallprice = models.DecimalField(max_digits=5, decimal_places=2)
    largeprice = models.DecimalField(max_digits=5, decimal_places=2)
    # display_order used to order items
    display_order = models.DecimalField(max_digits=7, decimal_places=3)

    class Meta:
        ordering = ['display_order']

    def get_absolute_url(self):
        """Returns the url to access a particular sub instance."""
        return reverse('dinnerplatter_detail', args=[str(self.id)])

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
    name = models.CharField(max_length=50, help_text='')
    customer_id = models.IntegerField(default = 0)
    #0: guest
    orderdate = models.DateTimeField(auto_now=False, auto_now_add=False)
    # Use customer_id and orderdate as keys
    foodtype = models.CharField(max_length=50, help_text='', default = '')
    foodname = models.CharField(max_length=100, help_text='')
    foodnameID = models.IntegerField(default = 0)
    toppings = models.CharField(max_length=100, default = '', help_text='', blank=True)
    foodprice = models.DecimalField(max_digits=5, decimal_places=2)
    qty = models.IntegerField(default = 0)
    foodrating = models.IntegerField(default = 0)
    # 0: no rating, -1: thumbs down, -2: thumbs up
    popularity = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    class Meta:
        ordering = ['-orderdate']
    # It is highlly unlikely that two orders will be submitted at the exact same time
    # so on need to sort by orderowner
    # It seems to me it is probably more efficient to sort by thumbs on
    # small database for customers viewing orders and the sort by rating
    # across the database by a manager will be infrequent

    def get_absolute_url(self):
        """Returns the url to access a particular pasta instance."""
        return reverse('order', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        #print("models 111: ",self)
        return self.name


class Rating(models.Model):
    """This model contains the ratings of customers for menu items. Maximum size
    is #Customers#MenuItems """
    customer_id = models.IntegerField(default = 0)
    foodtype = models.CharField(max_length=50, help_text='', default = '')
    foodnameID = models.IntegerField(default = 0)
    customer_rating = models.IntegerField(default = 0)
    foodname = models.CharField(max_length=100, default = '', help_text='', blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular rating instance."""
        return reverse('order', args=[str(self.id)])

    # def __str__(self): Commented out 2/24/2020
    #     """String for representing the Model object."""
    #     #print("models 111: ",self)
    #     return self.name
