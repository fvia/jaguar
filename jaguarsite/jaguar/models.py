import os
import os.path
import uuid


from django.db import models
from django.db.models.signals import pre_init, post_init, post_delete, post_save

from jaguarsite.settings import JAGUAR_FILES, JAGUAR_LINKS, JAGUAR_SITE

def strUuid():
    return str( uuid.uuid4())

################################

class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

#################################

class Archive(models.Model):
    filename = models.CharField( max_length=200 )
    status  = models.CharField( max_length=50, default = ''  )  # 'OK' | 'NO FILE'

    def __unicode__(self):
        return "{0} - {1}".format( self.filename, self.status)

def ArchivePostDelete( sender, **kwargs):
    instance = kwargs.get('instance')
    full_name = os.path.join( JAGUAR_FILES ,instance.filename )
    #print full_name
    os.unlink( full_name   )

post_delete.connect( ArchivePostDelete ,Archive)

#################################
class Link(models.Model):
    archive = models.ForeignKey(Archive)
    customer = models.ForeignKey(Customer)
    enabled = models.BooleanField( default= True )
    #expiryDate = models.DateField()
    # uuid hex format i.e. 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
    uuid =  models.CharField(max_length=36,db_index=True,default= lambda: str(uuid.uuid4()))
    status  = models.CharField( max_length=50, default = 'NEW'  )  #    'OK' | 'NO LINK'

    @property
    def url(self):
      return "http://{}/links/{}".format(JAGUAR_SITE,self.name_link())

    def __unicode__(self):
        return "{} - {} - {} - {} - {}".format(
            self.customer.name, self.archive.filename,
            self.uuid,self.status,
            self.url)
        #return "{} - {} - {} - {} - {}".format( "paco", "c:\\", self.expiryDate, self.uuid,self.statusname

    def name_link( self ):
        """ returns filename+uuid+extension
            p.e. from file:  'doc1.txt' with uuid 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
            -> doc1.d8e57661-7697-4a18-9067-bba5cad0f6dc.txt
        """
        (name,ext) = os.path.splitext( self.archive.filename )
        return "{}.{}{}".format( name,self.uuid,ext )   #ext ja porta el punt

def LinkPostSave( sender, **kwargs):
    """ after saving a Link if not exist a simbolic link to the file, its created
    """
    instance = kwargs.get('instance')
    source = os.path.join( JAGUAR_FILES ,instance.archive.filename )
    link_name = os.path.join( JAGUAR_LINKS ,instance.name_link() )
    if not os.path.exists(link_name ):
        os.symlink(source, link_name)
        instance.status = 'OK'
        instance.save()


def LinkPostDelete( sender, **kwargs):
    instance = kwargs.get('instance')
    full_name = os.path.join( JAGUAR_LINKS , instance.name_link() )
    #print full_name
    try:
        os.unlink( full_name   )
    except:
        pass

post_delete.connect( LinkPostDelete ,Link)
post_save.connect( LinkPostSave ,Link)

###################################################

class LinkHistory(models.Model):
    link = models.ForeignKey(Link)
    when = models.DateTimeField(db_index=True)
    ip   = models.GenericIPAddressField()

    def __unicode__(self):
        return "{} {}".format(self.when,self.ip)

################## git@github.com:fvia/jaguar.git
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
