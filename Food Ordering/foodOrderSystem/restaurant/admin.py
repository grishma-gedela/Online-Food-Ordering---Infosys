from django.contrib import admin
from restaurant.models import restaurantUser
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurantName','address','restaurantContact','email','password']

admin.site.register(restaurantUser,RestaurantAdmin)
