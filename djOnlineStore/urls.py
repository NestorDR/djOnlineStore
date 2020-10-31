"""
djOnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# Django is a high-level Python Web framework.
# django.contrib: this module has a variety of extra, optional tools that solve common Web-development problems.
from django.contrib import admin
# django.urls: this module has functions for use in URLconfs
from django.urls import include, path
# django.conf: this module allows to serve media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # include: is A function that takes a full Python import path to another URLconf module that should be “included”
    # in this place
    # Visit https://docs.djangoproject.com/en/3.1/ref/urls/#include
    path('', include('storeApp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
