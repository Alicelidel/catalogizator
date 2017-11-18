from django.contrib import admin
from .models import Arendator


# Register your models here.
@admin.register(Arendator)
class ArendatorAdmin(admin.ModelAdmin):
    list_display = ('person', 'has_pass', 'registered', 'ended')


#admin.site.register(Arendator)
