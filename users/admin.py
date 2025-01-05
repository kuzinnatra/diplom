from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone')
    list_filter = ('email', 'name', 'phone')
    search_fields = ('email', 'name', 'phone')
