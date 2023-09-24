from django.contrib import admin
from Project.models import ContactData,FormData

class ListModels(admin.ModelAdmin):
    list_display=['id','name',"email","message","datetime"]

admin.site.register(ContactData,ListModels)

class FormDataDisp(admin.ModelAdmin):
    list_display=['id']

# Register your models here.
