from django.db import models

# Create your models here.
class QuotesCollection(models.Model):
    quotes=models.TextField()
    author=models.CharField(max_length=50)
    class Meta:
        db_table="QuotesCollection"
        ordering=["author"]