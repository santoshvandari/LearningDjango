from django.contrib import admin
from Project.models import ContactData,FormData,ImageUpload,FileUpload

class ListModels(admin.ModelAdmin):
    list_display=['id','name',"email","message","datetime"]

admin.site.register(ContactData,ListModels)

class FormDataDisp(admin.ModelAdmin):
    list_display=['id','name',"email","message","datetime"]

admin.site.register(FormData,FormDataDisp)



class ImageUploadDisp(admin.ModelAdmin):
    list_display=['id','name','image']
admin.site.register(ImageUpload,ImageUploadDisp)

# Register your models here.

class FileUploadDisplay(admin.ModelAdmin):
        list_display=['id','name','file']
admin.site.register(FileUpload,ImageUploadDisp)
