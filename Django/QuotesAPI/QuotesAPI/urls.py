"""
URL configuration for QuotesAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('login/', admin.site.urls),
    path('home/',include("API.urls")),
    path('api/',include("API.urls")),
    path("",include("API.urls"))
]

# Change the Default ADIMN Text
admin.site.site_header = "Quotes API"
admin.site.site_title = "Quotes API Portal"
admin.site.index_title = "Welcome to Quotes API"