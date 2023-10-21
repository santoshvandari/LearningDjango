from django.contrib import admin
from API.models import PersonalInformation
# Register your models here.

class PersonalInformationModel(admin.ModelAdmin):
    list_display=["personalId","name","address","description","date"]
   
admin.site.register(PersonalInformation,PersonalInformationModel)
