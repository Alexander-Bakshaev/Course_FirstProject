from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, \
    HttpResponseBadRequest, HttpResponseForbidden


def index(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'blog/about.html')
