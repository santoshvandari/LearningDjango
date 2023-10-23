from django.db import models

# Create your models here.
class QuotesCollection(models.Model):
    quotes=models.TextField(blank=False,unique=True)
    author=models.CharField(max_length=50,default="Unknown")
    class Meta:
        db_table="QuotesCollection"
        ordering=["author"]
