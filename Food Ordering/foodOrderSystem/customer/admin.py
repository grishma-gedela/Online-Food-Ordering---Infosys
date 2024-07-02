from django.contrib import admin
from customer.models import customerUser,Feedback,Contact

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(customerUser,UserAdmin)
# Register your models here.
class Comments(admin.ModelAdmin):
    list_display = ['stars','comments']  

admin.site.register(Feedback, Comments)
admin.site.register(Contact)