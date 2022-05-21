from django.contrib import admin
from .models import Account

# Register your models here.

@admin.register(Account)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email", "date_joined", "last_login", "is_active", "is_admin", "is_superuser")
    search_fields = ("username", "email")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
