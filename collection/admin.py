from django.contrib import admin

# Register your models here.
from collection.models import Winery

class WineryAdmin(admin.ModelAdmin):
    model = Winery
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Winery, WineryAdmin)
