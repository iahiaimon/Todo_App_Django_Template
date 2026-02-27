from django.contrib import admin
from .models import CustomUser , Todo

# Register your models here.

admin.site.register(CustomUser)
# admin.site.register(Todo)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title",)
