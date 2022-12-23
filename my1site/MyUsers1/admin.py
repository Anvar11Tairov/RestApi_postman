from django.contrib import admin
from .models import MyUsers
# Register your models here.

class MyUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


admin.site.register(MyUsers, MyUsersAdmin)

