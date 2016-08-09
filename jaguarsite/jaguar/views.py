import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.

import tools
from jaguarsite.settings import JAGUAR_FILES
from jaguar.models import Archive, TrialExtension 


def index(request):
    return HttpResponse("")


def ReloadArchives(request):
    tools.register_Archives()
    disk_info = os.statvfs(JAGUAR_FILES)
    megabytes = disk_info.f_bsize * disk_info.f_bavail / 1.048576e6

    return HttpResponse(
        " Reload .... <BR>"
        " {:,.0f} MB available <BR>"
        " Done <BR> "
        " <a href='/jaguar/admin'> Back to Jaguar</a> ".format(megabytes)
        )


@login_required
def Downloads(request):
    archives = Archive.objects.filter(show_in_downloads=True)
    template = loader.get_template('downloads.html')
    context = RequestContext(
        request, 
        {'archives_list': archives}
    )
    return HttpResponse(template.render(context))


@login_required
def home(request):
    return HttpResponseRedirect( '/jaguar/downloads' )


def TrialExtensionGet(request):
    if 'trial_code' not in request.GET or 'machine_name' not in request.GET :
        return HttpResponse("ERROR#bad request")    
    
    code = request.GET['trial_code']
    res = TrialExtension.objects.filter( code = code  )
    if len(res) == 0:
        return HttpResponse("ERROR#unknown code")

    if res[0].applied==True:
        return HttpResponse("ERROR#code previosuly used")

    res[0].applied = True
    res[0].history = res[0].history + "\n" + str(datetime.datetime.now()) +"#GET#"+\
                        request.GET['machine_name'] + "#" +res[0].trialkey.name  
    res[0].save()


    res[0].save()
    return HttpResponse("OK#"+res[0].trialkey.v2c)

def TrialExtensionInfo(request):
    print request.GET
    if 'trial_code' not in request.GET or \
       'machine_name' not in request.GET or \
       'info'  not in request.GET :
        return HttpResponse("ERROR#bad request")    
    
    code = request.GET['trial_code']
    res = TrialExtension.objects.filter( code = code  )
    if len(res) == 0:
        return HttpResponse("ERROR#unknown code")

    res[0].history = res[0].history + "\n" + str(datetime.datetime.now()) +"#INFO#"+\
                        request.GET['machine_name'] + "#"+request.GET['info']  
    res[0].save()
    return HttpResponse("OK#DONE")