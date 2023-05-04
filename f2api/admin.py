from django.contrib import admin

from f2api.models import Profile

# Register your models here.

# @admin.register(Profile)

class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['id','folder_name', 'file']
    
admin.site.register(Profile,ProfileModelAdmin)