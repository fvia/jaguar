from django.db import models
import uuid
from django.db.models.signals import pre_init, post_init

def strUuid():
    return str( uuid.uuid4())


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name   

class Archive(models.Model):
    full_path = models.CharField( max_length=200 ) 
    
    def __unicode__(self):
        return self.full_path



class Link(models.Model):
    archive = models.ForeignKey(Archive)
    customer = models.ForeignKey(Customer)    
    expiryDate = models.DateField() 
    # uuid hex format i.e. 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
    uuid =  models.CharField(max_length=36,default= lambda: str(uuid.uuid4()))
    

    def __unicode__(self):
        return "{} - {} - {} - {}".format( self.customer.name, self.archive.full_path, self.expiryDate, self.uuid)
        #return "{} - {} - {} - {}".format( "paco", "c:\\", self.expiryDate, self.uuid)
         
##################
"""
def extraInitLink(sender,*args,**kwargs):
    instance = kwargs.get('instance')
    print( "s-->"+ str(sender) )
    print( "a-->"+ str(args) )
    print( "k-->"+ str(kwargs) )
    #if not hasattr(instance, 'uuid'):
    #     instance.uuid = 'calamar222'

def postInitLink(sender,*args,**kwargs):
    instance = kwargs.get('instance')
    print( "s-P>"+ str(sender) )
    print( "a-P>"+ str(args) )
    print( "k-P>"+ str(kwargs) )
    #if not hasattr(instance, 'uuid'):
    #     instance.uuid = 'calamar222'
    print( "instance.uuid :"+ str(instance.uuid) )
    print instance.uuid
    if instance.uuid == '':
      print "Bingo"
      instance.uuid == 'Bongo'
pre_init.connect(extraInitLink, Link)
post_init.connect(postInitLink, Link)
"""
