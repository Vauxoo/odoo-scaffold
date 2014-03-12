#!/usr/bin/python
import os
import pprint


class Repository(object):

    def __init__(self, name, serie, group, local_path, cloud_url=False):
        """
        Inicializate the repository object with the corresponding data
        @param name: name of the repository given for the user.
        @param serie: number of the project serie (the branch of the project
                      to push).
        @param group: launchpad group with permissions to push to the branch.
        @param local_path: the path of your local copy of the repository.
        @param cloud_url: the path of your local copy of the repository.
        """
        self.name = name
        self.serie = serie
        self.group = group
        self.local_path = local_path
        self.cloud_url = cloud_url
        # self.check_repo_local_path()

    def check_repo_local_path(self):
        """
        Check that the local repo given it really exist
        @return: True if exist, False if not exist.
        """
        if not os.path.exists(self.local_path):
            print ('The %s repository can be used because the local path'
                   ' given really do no exist.' % (name, ))
            return False
        return True


class Config(object):

    def __init__(self):
        """
        Create a config Object from openerp module. it set by default the
        repositories
        """
        self.repositories = {
            'addons-vauxoo': Repository(
                name='addons-vauxoo',
                serie='7.0',
                group='~vauxoo',
                local_path='/home/kathy/bzr_projects/addons_vauxoo/7.0'),
            'vauxoo-private': Repository(
                name='vauxoo-private',
                serie=False,
                group='~vauxoo-private',
                local_path='/home/kathy/bzr_projects/vauxoo_private'),
            'ovl70': Repository(
                name='openerp-venezuela-localization',
                serie='7.0',
                group='~vauxoo',
                local_path='/home/kathy/bzr_projects/_VE/ovl_branches/ovl70'),
            'junk': Repository(
                name='+junk',
                serie='oerpmodule_test',
                group='~kathy-zaoral',
                local_path='/home/kathy/bzr_projects/+junk/kathy-zaoral/oerpmodule_test'),
        }

    def print_repositories(self):
        """
        Print the data of the repositories
        """
        print '\nCurrent configured repositories:'
        for (repo, values) in self.repositories.iteritems():
            print '\n%s' % (repo,)
            pprint.pprint(values.__dict__)
        print '\n'
        return True

    def get_repositories_names(self):
        """
        Reutrn a list of string the the current saved repositories
        """
        return self.repositories.keys()
