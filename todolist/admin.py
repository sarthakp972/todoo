from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TODOO  # import your model

@admin.register(TODOO)
class TODOOAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'user', 'date')  # fields to display in the list view
    search_fields = ('title', 'user__username')       # enable search
    list_filter = ('date', 'user')                    # optional filters in the right sidebar
