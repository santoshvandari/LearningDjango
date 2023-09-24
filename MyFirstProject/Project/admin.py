from django.contrib import admin
from Project.models import ContactData

class ListModels(admin.ModelAdmin):
    list_display=['name',"email","message","datetime"]

admin.site.register(ContactData,ListModels)

# Register your models here.
