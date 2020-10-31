# Django is a high-level Python Web framework.
# django.db: this module is provided as a database wrapper, use it for ORM (Object Relational Mapping)
# Visit: https://docs.djangoproject.com/en/3.1/topics/db/
from django.db import models
# django.contrib: this module has a variety of extra, optional tools that solve common Web-development problems.
# auth.models.User: this module allow access to users of the database
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    """
     Specify as variables, the fields that compose the Services object/table in database.
     Visit: https://docs.djangoproject.com/en/3.1/topics/db/models/
    """
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='services')
    # If you want to add "create" and "update" time logging to your model, it's as simple as:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Internal class for applying metadata on fields
        Visit: https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options
        """
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.title


class Category(models.Model):
    """
     Specify as variables, the fields that compose the Services object/table in database.
     Visit: https://docs.djangoproject.com/en/3.1/topics/db/models/
    """
    name = models.CharField(max_length=50)
    # If you want to add "create" and "update" time logging to your model, it's as simple as:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Internal class for applying metadata on fields
        Visit: https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options
        """
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
     Specify as variables, the fields that compose the Services object/table in database.
     Visit: https://docs.djangoproject.com/en/3.1/topics/db/models/
    """
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    # null=True, blank=True for optional or nullable values in field
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    # Foreign key field. If the referenced entity is deleted,
    #  it will trigger the delete on related records in this object / table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    # If you want to add "create" and "update" time logging to your model, it's as simple as:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Internal class for applying metadata on fields
        Visit: https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options
        """
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
