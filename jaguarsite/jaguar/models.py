import os
import os.path
import uuid


from django.db import models
from django.db.models.signals import pre_init, post_init

def strUuid():
    return str( uuid.uuid4())


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Archive(models.Model):
    filename = models.CharField( max_length=200 )
    status  = models.CharField( max_length=50, default = ''  )  # 'OK' | 'NO FILE'

    def __unicode__(self):
        return "{0} - {1}".format( self.filename, self.status)



class Link(models.Model):
    archive = models.ForeignKey(Archive)
    customer = models.ForeignKey(Customer)
    expiryDate = models.DateField()
    # uuid hex format i.e. 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
    uuid =  models.CharField(max_length=36,default= lambda: str(uuid.uuid4()))
    status  = models.CharField( max_length=50, default = 'NEW'  )  #    'OK' | 'NO LINK'

    def __unicode__(self):
        return "{} - {} - {} - {} - {}".format( self.customer.name, self.archive.filename, self.expiryDate, self.uuid,self.status)
        #return "{} - {} - {} - {} - {}".format( "paco", "c:\\", self.expiryDate, self.uuid,self.statusname

    def name_link( self ):
        """ returns filename+uuid+extension
            p.e. from file:  'doc1.txt' with uuid 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
            -> doc1.d8e57661-7697-4a18-9067-bba5cad0f6dc.txt
        """
        (name,ext) = os.path.splitext( self.archive.filename )
        return "{}.{}{}".format( name,self.uuid,ext )   #ext ja porta el punt

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
