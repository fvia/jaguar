import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

import tools
from jaguarsite.settings import JAGUAR_FILES
from jaguar.models import Archive


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


def Downloads(request):
    archives = Archive.objects.all()
    template = loader.get_template('downloads.html')
    context = RequestContext(
        request, 
        {'archives_list': archives}
    )
    return HttpResponse(template.render(context))

    
