from django.contrib import admin
from .models import Games

# Register your models here.
class GamesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'platform', 'Devs', )
    list_display = ('name', 'platform', 'release_date', 'Devs', 'weighed_score', 'featured')

admin.site.register(Games, GamesAdmin)
