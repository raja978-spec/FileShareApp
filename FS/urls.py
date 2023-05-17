"""
URL configuration for FS project.

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
from SharingApp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
          path('admin/', admin.site.urls),
          path('',views.register,name='register'),
          path('login',views.login,name='login'),
          path('forgot-password',views.For,name='forgot-password'),
          path('home/<i>',views.home,name='home'),
        path('logout',views.logout,name='logout'),
        path('fileupload/<i>',views.fileupload,name='fileupload'),
        path('seefile/<i>',views.seefile,name='seefile'),
        path('delete/<i>',views.delete,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
