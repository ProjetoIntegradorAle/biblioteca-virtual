from django.contrib import admin
from .models import User, FraseDoDia
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)

@admin.register(FraseDoDia)
class FraseDoDiaAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'autor')
    list_filter = ('dia_semana',)
