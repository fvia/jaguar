import os
import datetime
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from jaguarsite.settings import JAGUAR_KEY_UPDATES


# Create your views here.

import tools
from jaguarsite.settings import JAGUAR_FILES
from jaguar.models import Archive, TrialExtension, Customer
from jaguar.models import LicenseKey, LicenseKeyUpdate



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


def LoadStuff(request):  # called by LoadKeyUpdates
    files = os.listdir(JAGUAR_KEY_UPDATES)
    for f in files:
        if f.endswith('.V2C'):
            filename,extension = os.path.splitext(f) 
            if not LicenseKey.objects.filter(key_id=request.GET['customers']).exists():
                cu = Customer.objects.filter(name=request.GET['customers'])[0]

                lk = LicenseKey( key_id=filename, customer=cu )
                lk.save()    

            lk = LicenseKey.objects.get(key_id=filename)
            file_content= open(  os.path.join(JAGUAR_KEY_UPDATES,f)  ).read()
            lku = LicenseKeyUpdate( key_id=lk, v2c=file_content )
            lku.save()

            # after the content has been loaded delete the file
            os.remove(os.path.join(JAGUAR_KEY_UPDATES,f))

   
def ClearKeyUpdateDir(): # called by LoadKeyUpdates
    files = os.listdir(JAGUAR_KEY_UPDATES)
    for f in files:
        os.remove(os.path.join(JAGUAR_KEY_UPDATES,f))



def LoadKeyUpdates(request):
    if 'cleardir' in request.GET: 
        ClearKeyUpdateDir()

    if 'customers' in request.GET: 
        LoadStuff(request)

    customers = Customer.objects.order_by('name')
    strCustomerOptions =""
    for c in customers:
        strCustomerOptions +=  '<option value="{}">{}</option>'.format( c.name,c.name)

    strFiles = '<table style="border: 1px black solid;" ><tr><th>V2C Files in folder {} </th></tr>'.format(JAGUAR_KEY_UPDATES)
    files = os.listdir(JAGUAR_KEY_UPDATES)
    if len(files) == 0:
        strFiles += '<tr><td>No files found</td></tr>'
    for f in files:
        if f.endswith('.V2C'):
            strFiles += '<tr><td>{}</td></tr>'.format(f)
    
    strFiles += "</table>" 

    return HttpResponse(
        "<H1> Key Updates</H1> "
        ""
        '<table><tr>'
        '<td style="border: 4px brown solid;"><a href="/jaguar/admin"> Back to Jaguar</a></td> '
        '<td style="border: 4px brown solid;"><a href="/jaguar/jg/LoadKeyUpdates"> Refresh </a></td> '
        '<td style="border: 4px brown solid;"><a href="/jaguar/jg/LoadKeyUpdates?cleardir=true"> Delete All Files </a></td>'
        '</tr></table>'
        ""
        +strFiles+

        "<p> 'Load' will read every V2C file, create a LicenseKey record if not exist, "
        "and create a KeyUpdate record, after thar the  V2C file will be deleted  "
        "</p>"
        "<form>"
        'Customer: <select name="customers">'+
        strCustomerOptions+
        '</select>'
        '<input type="submit" value="Load"> '
        "</form>"    
        

        )




@login_required
def Downloads(request):
    archives = Archive.objects.filter(show_in_downloads=True)
    template = loader.get_template('downloads2.html')
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



def LicenseUpdateGet(request):
    if 'key_id' not in request.GET or \
       'machine_name' not in request.GET or \
       'release' not in request.GET :
        return HttpResponse("BAD_REQUEST#bad request")    
    
    code = request.GET['key_id']
    kus =  LicenseKeyUpdate.objects.filter(key_id = code).order_by('-time_uploaded')
    if len(kus) == 0:
        return HttpResponse("UNKNOWN_CODE#Key Code Unknown")        
    ku = kus[0]  
    key =  ku.key_id

    if ku.applied:
        key.history += str(datetime.datetime.now()) +"#GET#"+\
                    request.GET['machine_name'] + "#"+request.GET['release'] +\
                    "ALREADY_APPLIED#\n"

        return HttpResponse("ALREADY_APPLIED#Key Code already applied")        

    
    key.history += str(datetime.datetime.now()) +"#GET#"+\
                    request.GET['machine_name'] + "#"+request.GET['release'] +\
                    "#OK\n"
    key.save()                

    return HttpResponse("OK#"+ku.v2c)


def LicenseUpdateInfo(request):
    if 'key_id' not in request.GET or \
       'machine_name' not in request.GET or \
       'release' not in request.GET or \
       'info' not in request.GET :
        return HttpResponse("BAD_REQUEST#bad request")    
 
    code = request.GET['key_id']
    kus =  LicenseKeyUpdate.objects.filter(key_id = code).order_by('-time_uploaded')
    if len(kus) == 0:
        return HttpResponse("UNKNOWN_CODE#Key Code Unknown")        
    ku = kus[0]  
    key =  ku.key_id

    if request.GET['info'] == 'StatusOk':
        ku.applied = True
        ku.save()
	
    key.history += str(datetime.datetime.now()) +"#INFO#"+\
                    request.GET['machine_name'] + "#"+request.GET['release'] +\
                    "#"+request.GET['info']+"\n"
    key.save()                

    print "adeu"


    return HttpResponse("OK#DONE")
