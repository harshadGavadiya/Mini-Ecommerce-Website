
from django.contrib import admin
from EcommarceWebsite.models import Information

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display = ['Title']

admin.site.register(Information,InformationAdmin)