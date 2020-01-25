from django.contrib import admin

# Register your models here.
from orders.models import Regularpizza, Topping, Pasta, Salad, Sub, Dinnerplatter, Order, Rating

@admin.register(Regularpizza) # @ decorator does exactly the same thing as the admin.site.register() syntax
class RegularpizzaAdmin(admin.ModelAdmin):
    pass

@admin.register(Topping) # @ decorator does exactly the same thing as the admin.site.register() syntax
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Salad) # @ decorator does exactly the same thing as the admin.site.register() syntax
class SaladAdmin(admin.ModelAdmin):
    pass


@admin.register(Pasta) # @ decorator does exactly the same thing as the admin.site.register() syntax
class PastaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sub) # @ decorator does exactly the same thing as the admin.site.register() syntax
class SubAdmin(admin.ModelAdmin):
    pass

@admin.register(Dinnerplatter) # @ decorator does exactly the same thing as the admin.site.register() syntax
class SubAdmin(admin.ModelAdmin):
    pass

@admin.register(Order) # @ decorator does exactly the same thing as the admin.site.register() syntax
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating) # @ decorator does exactly the same thing as the admin.site.register() syntax
class RatingAdmin(admin.ModelAdmin):
    pass
