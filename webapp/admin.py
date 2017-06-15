from django.contrib import admin

# Register your models here.
from webapp import models
from _csv import list_dialects

class useradmin(admin.ModelAdmin):
    list_display=('username','password','email','user_type')
    search_fields=('username','password','email','user_type')
#     search_fields=('hostname','provice')
    list_filter=('username','password','email','user_type')
class usertypeadmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(models.user,useradmin)
admin.site.register(models.usertype,usertypeadmin)

