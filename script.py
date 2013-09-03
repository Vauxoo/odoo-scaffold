# bin/python
import os

class new_openerp_module:

    directory_list = [
        'model',
        'view',
        'workflow',
        'i18n',
        'wizard',
        'data',
        'demo',
        'static',
        'static/src',
        'static/src/img']

    name = False,
    version = False
    developer = 'kty'

    def __init__(self, name, developer, version='7.0'):
        """
        iniciialization of the module
        @param name: new module name
        @param version: the version of the new model
        @param developer:
        """

        print '\n'*2
        print '__init__()'

        self.name = name,
        self.version = version,
        self.developer = developer,
        self.directory = '%s-dev-%s-%s' % (version, name, developer)

        #~ TODO: make a restriction that only can create module in the set of 
        #~ real version 6.0 6.1 and 7.0

    def create_main_directory(self):
        """
        """
        exit_status = os.system('mkdir %s' % (self.directory,))
        
    def create_directories(self):
        """
        create the base directories taking into account the direcotory config
        list
        """
        for directory in self.directory_list:
            exit_status = os.system('mkdir %s/%s' % (self.directory, directory))
        return True

module = new_openerp_module('xxy', 'kty')
module.create_main_directory()
module.create_directories()