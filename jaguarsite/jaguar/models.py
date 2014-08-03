import os
import os.path
import uuid

from django.db import models
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import post_delete, post_save

from jaguarsite.settings import JAGUAR_FILES, JAGUAR_LINKS, JAGUAR_SITE


class Customer(models.Model):
    """
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Archive(models.Model):
    """
    """
    filename = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='')  # 'OK' | 'NO FILE'

    def __unicode__(self):
        return "{0}".format(self.filename)


def ArchivePostDelete(sender, **kwargs):
    instance = kwargs.get('instance')
    full_name = os.path.join(JAGUAR_FILES, instance.filename)
    try:
        os.unlink(full_name)
    except:
        pass

post_delete.connect(ArchivePostDelete, Archive)


class Link(models.Model):
    """
    """
    archive = models.ForeignKey(Archive)
    customer = models.ForeignKey(Customer)
    enabled = models.BooleanField(default=True)
    # expiryDate = models.DateField()
    # uuid hex format i.e. 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
    uuid = models.CharField(
        max_length=36,
        db_index=True,
        default=lambda: str(uuid.uuid4())
        )
    status = models.CharField(max_length=50, default='NEW')  # 'OK' | 'NO LINK'

    @property
    def url(self):
        return "http://{}/links/{}".format(JAGUAR_SITE, self.name_link())

    def __unicode__(self):
        return "{} - {} - {} - {} - {}".format(
            self.customer.name, self.archive.filename,
            self.uuid, self.status,
            self.url)

    def name_link(self):
        """ returns filename+uuid+extension
            p.e. from file:
            'doc1.txt' with uuid 'd8e57661-7697-4a18-9067-bba5cad0f6dc'
            -> doc1.d8e57661-7697-4a18-9067-bba5cad0f6dc.txt
        """
        (name, ext) = os.path.splitext(self.archive.filename)
        return "{}.{}{}".format(name, self.uuid, ext)   # ext ja porta el punt


def LinkPostSave(sender, **kwargs):
    """ after saving a Link if not exist a simbolic link to the file,
        its created
    """
    instance = kwargs.get('instance')
    source = os.path.join(JAGUAR_FILES, instance.archive.filename)
    link_name = os.path.join(JAGUAR_LINKS, instance.name_link())

    if instance.enabled:
        if not os.path.exists(link_name):
            os.symlink(source, link_name)
            instance.status = 'OK'
            instance.save()
    else:
        try:
            os.unlink(link_name)
        except:
            pass


def LinkPostDelete(sender, **kwargs):
    instance = kwargs.get('instance')
    full_name = os.path.join(JAGUAR_LINKS, instance.name_link())
    # print full_name
    try:
        os.unlink(full_name)
    except:
        pass

post_delete.connect(LinkPostDelete, Link)
post_save.connect(LinkPostSave, Link)


class LinkHistory(models.Model):
    """
    """
    link = models.ForeignKey(Link)
    when = models.DateTimeField(db_index=True)
    ip = models.GenericIPAddressField()

    def __unicode__(self):
        return "{} {}".format(self.when, self.ip)

    def FileName(self):
        return self.link.archive.filename

    def CustomerName(self):
        return self.link.customer.name
