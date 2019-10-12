from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email', 'phone_num', 'gender')
    list_display_links=('first_name', 'last_name', 'email', 'phone_num', 'gender')
    search_fields=('first_name', 'last_name', 'email', 'phone_num', 'gender')
    list_per_page=25
admin.site.register(User, UserAdmin)
