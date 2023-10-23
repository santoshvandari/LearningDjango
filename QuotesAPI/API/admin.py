from django.contrib import admin
from API.models import QuotesCollection

# Register your models here.
class DisplayQuotesData(admin.ModelAdmin):
    list_display=["id","quotes","author"]

admin.site.register(QuotesCollection,DisplayQuotesData)
