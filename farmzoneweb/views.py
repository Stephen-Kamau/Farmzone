# Create your views here.
from django.shortcuts import render


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'index.html')


def about(request):
    """

    :param request:
    :return:
    """
    return render(request, 'about.html')


def contact(request):
    """

    :param request:
    :return:
    """
    return render(request, 'contact.html')


def forum(request):
    """

    :param request:
    :return:
    """
    return render(request, 'forum.html')


def listings(request):
    """

    :param request:
    :return:
    """
    return render(request, 'listings.html')


def listing_single(request):
    """

    :param request:
    :return:
    """
    return render(request, 'listings-single.html')


def login(request):
    """

    :param request:
    :return:
    """
    return render(request, 'login.html')


def post_item(request):
    """

    :param request:
    :return:
    """
    return render(request, 'postitem.html')


def profile(request):
    """

    :param request:
    :return:
    """
    return render(request, 'profile.html')


def register(request):
    """

    :param request:
    :return:
    """
    return render(request, 'register.html')
