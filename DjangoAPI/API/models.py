from django.db import models

# Create your models here.
# class PersonalInformation(models.Model):
#     personalId = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     description = models.TextField()
#     date = models.DateField(auto_now=True)
#     class Meta:
#         db_table = "PersonalInformation"
#         ordering = ["date"]


class StudentInformation(models.Model):
    studentId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    grade=models.IntegerField()
    date=models.DateField(auto_now=True)
    class Meta:
        db_table='StudentData'

