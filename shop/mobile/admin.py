from django.contrib import admin
from .models import Mobile
# Register your models here.

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display=('name','price','storage','created')
    list_filter=('name','price')
    list_editable=('price','storage')
    search_fields=('name','price')