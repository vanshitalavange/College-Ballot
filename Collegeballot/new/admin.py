# Register your models here.
from django.contrib import admin
from . models import Data,Hod
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(Data)
@admin.register(Data)
class student(ImportExportModelAdmin):
    pass

@admin.register(Hod)
class hod(ImportExportModelAdmin):
    pass