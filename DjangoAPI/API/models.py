from django.db import models

# Create your models here.
class PersonalInformation(models.Model):
    personalId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField(auto_now=True)
    class Meta:
        db_table="PersonalInformation",
        ordering = ["date"]
