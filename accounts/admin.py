from django.contrib import admin
from .models import NormalUser

@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_verified', 'created_at')
    search_fields = ('email',)
