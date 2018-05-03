from django.contrib import admin
from .models import Novel

class BbsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)

admin.site.register(Novel,BbsAdmin)
