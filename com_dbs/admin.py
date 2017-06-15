from django.contrib import admin

# Register your models here.
from com_dbs import models

class python_stru_admin(admin.ModelAdmin):
    list_display=('title_level',)
class python_title_admin(admin.ModelAdmin):
    list_display=('title','t_level','pre_title','note_date','visit_count')
    search_fields=('title','t_level','pre_title','note_date','visit_count')
    list_filter=('title','t_level','pre_title','note_date','visit_count')
class python_cont_admin(admin.ModelAdmin):
    list_display=('cont_title','cont_py')

admin.site.register(models.python_stru,python_stru_admin)
admin.site.register(models.python_title,python_title_admin)
admin.site.register(models.python_cont,python_cont_admin)