from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()
    datetime = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table="ContactData"
        get_latest_by = "datetime"
        

class FormData(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()
    datetime = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table="FormData"



class ImageUpload(models.Model):
    name=models.CharField(max_length=30)
    image=models.FileField(upload_to="images", max_length=20,default=None, null=True)
    class Meta:
        db_table="ImageUpload"
        get_latest_by = "datetime"


class FileUpload(models.Model):
    name=models.CharField(max_length=30)
    file=models.FileField(upload_to="files", max_length=50,default=None, null=True)
    class Meta:
        db_table="FileUpload"
        get_latest_by = "datetime"


class UserData(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(Null=False)
