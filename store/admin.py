from django.contrib import admin

from store.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price',)
    list_filter = ('name',)
