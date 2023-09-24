from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()

    class Meta:
        db_table="ContactData"
