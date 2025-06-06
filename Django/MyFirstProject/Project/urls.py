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
from django.urls import path
# from MyFirstProject import views
from Project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='root'),
    path('home/',views.home,name='home'),
    # path('loop/',views.loop),
    # path('ifelse/',views.ifelse),
    path('contact/',views.contact,name="contact"),
    path('services/',views.services),
    path('about/',views.about),
    path('form/',views.form,name='form'),
    path('submit/',views.submit,name='submit'),
    path('formdata/',views.formdata,name='formdata'),
    path('file/',views.file,name='file'),
    path('login/',views.loginUser,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logoutUser,name="logout"),








    # path('admin/', admin.site.urls),
    # path('dynamic/',views.DynamicUrl,name='DynamicUrl'),
    # path('dynamic/<data>/',views.DynamicContent,name="DynamicContent")
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)