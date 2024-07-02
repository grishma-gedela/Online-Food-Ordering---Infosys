from django.contrib import admin
from restaurant.views import foodItems

class ItemsList(admin.ModelAdmin):
    list_display = ['name','price','image','restaurantName']  

admin.site.register(foodItems, ItemsList)