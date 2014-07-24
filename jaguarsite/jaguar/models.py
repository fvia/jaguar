from django.db import models

# Create your models here.

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

    def __unicode__(self):
        return "{} - {} - {}".format( self.customer.name, self.archive.full_path, self.expiryDate)    

