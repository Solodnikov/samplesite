from django.contrib import admin

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'price','rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    empty_value_display = '-пусто-'


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
