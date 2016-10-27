from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.context import RequestContext
from django.template import Template

# Create your views here.


def index(request):
    return HttpResponse(Template(open('euler/templates/index.html').read()).render(RequestContext(request)))


def login_page(request):
    if request.method == 'GET':
        return HttpResponse(Template(open('euler/templates/login.html').read()).render(RequestContext(request)))

    elif request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                     password=request.POST['password'])


        if user is not None:
            login(request, user)

            return HttpResponseRedirect('../examine/dashboard')

        else:
            return HttpResponse(Template(open('euler/templates/login.html').read()).render(RequestContext(request)))