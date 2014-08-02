import os
import os.path

from jaguarsite.settings import JAGUAR_FILES, JAGUAR_LINKS
from jaguar.models import Archive, Link


def register_Archives():
    """ register all not registered files as Archives,
        in the JAGUAR_FILES folder
    """
    files_on_folder = [
        f for f in os.listdir(JAGUAR_FILES)
        if os.path.isfile(os.path.join(JAGUAR_FILES, f))
        ]

    set_files_on_folder = set(files_on_folder)
    # print(str(files_on_folder))

    files_on_archives = [a.filename for a in Archive.objects.all()]
    set_files_on_archives = set(files_on_archives)
    # print(str(files_on_archives))

    # if some files on folder are not registered we add to Archives
    files_to_add = set_files_on_folder - set_files_on_archives
    print(str(files_to_add))
    for f in files_to_add:
        a = Archive()
        a.filename = f
        a.status = 'OK'
        a.save()


def status_Archives():
    """
    """
    for a in Archive.objects.all():
        if os.path.isfile(os.path.join(JAGUAR_FILES, a.filename)):
            a.status = 'OK'
        else:
            a.status = 'NO FILE'
        a.save()


def create_Links():
    """ create symbolics links on JAGUAR_LINKS,
        for every Link that not has an associated symbolic link.
    """
    for l in Link.objects.all():
        source = os.path.join(JAGUAR_FILES, l.archive.filename)
        link_name = os.path.join(JAGUAR_LINKS, l.name_link())
        print source
        print link_name
        if not os.path.exists(link_name):
            os.symlink(source, link_name)
            l.status = 'OK'
            l.save()


def delete_Links():
    """ deletes the orphan symbolic links ( not pointed for any Link)
    """
    links_on_folder = [
        l for l in os.listdir(JAGUAR_LINKS)
        if os.path.islink(os.path.join(JAGUAR_LINKS, l))
        ]
    links_on_folder = set(links_on_folder)

    links_on_app = [l.name_link() for l in Link.objects.all()]
    links_on_app = set(links_on_app)

    links_to_delete = links_on_folder - links_on_app

    for l in links_to_delete:
        os.remove(os.path.join(JAGUAR_LINKS, l))
