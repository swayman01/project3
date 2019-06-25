from django.contrib import admin

# Register your models here.
from orders.models import Salad
@admin.register(Salad) # @ decorator does exactly the same thing as the admin.site.register() syntax
class Salad(admin.ModelAdmin):
    pass

# @admin.register(Salads) # @ added for rename error
# class Salads(admin.ModelAdmin):
#     pass
