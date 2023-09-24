from django.contrib import admin
from Project.models import ContactData,FormData

class ListModels(admin.ModelAdmin):
    list_display=['id','name',"email","message","datetime"]

admin.site.register(ContactData,ListModels)

class FOrm

# Register your models here.
