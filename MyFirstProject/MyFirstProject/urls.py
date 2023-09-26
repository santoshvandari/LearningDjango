"""
URL configuration for MyFirstProject project.

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
# from MyFirstProject import views
# from Project import urls


urlpatterns = [
    path('admin/',admin.site.urls),
    # path('admin/',include('Project.urls')),
    path('',include('Project.urls')),
    path('home/',include('Project.urls')),
    # path('loop/',include('Project.urls')),
    # path('ifelse/',include('Project.urls')),
    path('contact/',include('Project.urls')),
    path('services/',include('Project.urls')),
    path('about/',include('Project.urls')),
    path('form/',include('Project.urls')),
    path('submit/',include('Project.urls')),
    path('formdata/',include('Project.urls')),
    path('file/',include('Project.urls')),
    path('login/',include('Project.urls')),
    path('logout/',include("Project.urls")),
  












    # path('admin/', admin.site.urls),
    # path('dynamic/',views.DynamicUrl,name='DynamicUrl'),
    # path('dynamic/<data>/',views.DynamicContent,name="DynamicContent")
]

admin.site.site_header = "Santosh Login"
admin.site.site_title = "Santosh Website"
admin.site.index_title = "Welcome to Santosh Billing System"
handler404 = 'Project.views.custom404'