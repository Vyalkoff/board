from django.contrib import admin
from .models import Adt
from .models import Rubric


# Register your models here.

class AdtAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Adt, AdtAdmin)
admin.site.register(Rubric)
