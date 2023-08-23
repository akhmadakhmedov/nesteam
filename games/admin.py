from django.contrib import admin
from .models import Game, Studio, Genre



admin.site.register(Game)
admin.site.register(Genre)


class GameInline(admin.StackedInline):
    model = Game
    extra = 0

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'workers_count']
    inlines = [GameInline]

