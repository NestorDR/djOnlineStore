# django.urls: is a library that offers functions for use in URLconfs
from django.urls import path

from . import views

# urlpatterns: List to be included in main configuration URLconf (in urls.py of the project)
# Visit: https://docs.djangoproject.com/en/3.1/ref/urls/#include
urlpatterns = [
    path('', views.home, name='Home'),
    path('services/', views.services, name='Services'),
    path('store/', views.store, name='Store'),
    path('blog/', views.blog, name='Blog'),
    path('blog/category/<int:category_id_>/', views.category, name='Category'),
    path('contact/', views.contact, name='Contact'),
]
