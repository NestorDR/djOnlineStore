# datetime: this module supplies classes for manipulating dates and times.
import datetime as dt
# django.http: Django uses request and response objects to pass state through the system.
from django.http import HttpRequest, HttpResponse
# django.shortcuts: is a library that collects helper functions and classes that “span” multiple levels of MVC
from django.shortcuts import render

from .models import Category, Post, Service


def __function_name():
    """
    This function will return the caller's function name.
    """
    # Traceback: this module provides a standard interface to extract, format and print stack traces of Python programs
    import traceback

    return traceback.extract_stack(None, 2)[0][2]


def __common_context() -> dict:
    """
    Create common web context for every view, with a dictionary.

    :return: A web context dict
    """
    now_ = dt.datetime.now()
    return dict(
        year=now_.year,
    )


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    Create home view.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Select template
    template_ = 'home.html'

    # return HttpResponse object resulting of render method
    return render(request, template_)


def services(request: HttpRequest) -> HttpResponse:
    """
    Create services view.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Get objects/rows of Service class
    services_ = Service.objects.all()

    # Select template
    template_ = 'services.html'

    # Create web context
    context_ = __common_context()
    context_['services'] = services_

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def store(request: HttpRequest) -> HttpResponse:
    """
    Create store view.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Select template
    template_ = 'store.html'

    # return HttpResponse object resulting of render method
    return render(request, template_)


def blog(request: HttpRequest) -> HttpResponse:
    """
    Create blog view.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Get ten firs objects/rows of Post class, sorted by update date
    posts_ = Post.objects.all().order_by('-updated')[:10]

    # Select template
    template_ = 'blog.html'

    # Create web context
    context_ = __common_context()
    context_['posts'] = posts_

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def category(request: HttpRequest,
             category_id_: int) -> HttpResponse:
    """
    Create blog view.

    :param request: HttpRequest object with metadata about the request
    :param category_id_: category identifier

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Get objects/rows of Post class
    category_ = Category.objects.get(id=category_id_)
    filtered_posts_ = Post.objects.filter(categories=category_).order_by('-updated')[:10]

    # Select template
    template_ = 'category.html'

    # Create web context
    context_ = __common_context()
    context_['category'] = category_
    context_['posts'] = filtered_posts_

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def contact(request: HttpRequest) -> HttpResponse:
    """
    Create contact view.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # Select template
    template_ = 'contact.html'

    # return HttpResponse object resulting of render method
    return render(request, template_)
