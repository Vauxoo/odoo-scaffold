#!/usr/bin/python
import os
import sys
from config import *


class Module(object):

    directory_list = [
        'model',
        'view',
        'wizard',
        'i18n',
        'workflow',
        'data',
        'demo',
        'doc',
        'doc/images',
        'test',
        'report',
        'security',
        'static',
        'static/description',
        'static/src',
        'static/src/js',
        'static/src/css',
        'static/src/xml',
        'static/src/img']

    def __init__(self, name, module_developers, module_planners,
                 module_auditors, folder=None):
        """
        iniciialization of the module
        @param name: new module name
        """

        #~ TODO: add the manage a list of developers, planners and auditors

        print '\n... Checking Script Parameters'
        self.name = name.split('/')[-1]
        self.path = '%s/%s' % (folder, name)

        self.module_developers = module_developers
        self.module_planners = module_planners
        self.module_auditors = module_auditors

        #print ' ====== module object '
        #import pprint
        #pprint.pprint(self.__dict__)
        return None


    def create_main_directory(self):
        """
        Create the module main directory with the module name.
        """
        print '... Create module main directory'
        os.system('mkdir %s' % (self.path))
        return True

    def create_directories(self):
        """
        Create the base directories taking into account the directory config
        list.
        """
        print '... Create module structure dicectories'
        for strc_dir in self.directory_list:
            os.system('mkdir %s/%s' % (self.path, strc_dir))
        return True

    def create_base_files(self):
        """
        Create the base files for the module, include de init files, the
        openerp file and the index.html and the icon.png file.
        """
        print '... Create module base files'
        self.create_init_files()
        self.create_openerp_file()
        self.add_icon_file()
        self.create_index_html_file()
        return True

    def create_init_files(self):
        """
        Create init files with the license set taking into account the module
        developers, planners and auditors.
        """
        print '... Creating init files'
        self.create_file('__init__.py', '__init__.py', False)
        self.create_file(False, '__init__.py', 'model')
        self.create_file(False, '__init__.py', 'wizard')
        return True

    def create_openerp_file(self):
        """
        Create the openerp descriptive file
        """
        print '... Create the openerp descriptive file'
        self.create_file('__openerp__.py', '__openerp__.py', False)
        return True

    def create_file(self, template_name, new_file, file_dir=False):
        """
        Create a new file. First concatenate the content of the required
        templates and generate the file in the new module corresponding
        directory folder. And then convert the generate template like file
        into the real file with the module data.
        @param template_name: string with the name of the template to create,
            complete name with the file extenesion
        """
        this_dir, this_filename = os.path.split(__file__)
        data_dir = "/".join([this_dir, 'data'])
        file_dir = file_dir and '/'.join([self.path, file_dir]) or self.path
        new_file_full_path = '/'.join([file_dir, new_file])
        
        template_file = \
            template_name and '/'.join([data_dir, template_name]) or ''

#        print 'this_dir', this_dir
#        print 'data_dir', data_dir 
#        print 'file_dir', file_dir 
#        print 'new_file', new_file_full_path
#        print 'template', template_name
#        print 'template_file', template_file

        os.system("cat %s/license_msg.py %s > %s" % (
            data_dir, template_file, new_file_full_path))
        file_name = getattr(self, 'file_name', '__NO_DEFINED__') 
        var_value_dict = {
            '__OERPMODULE_CLASS_NAME__': file_name,
            '__OERPMODULE_MODEL_NAME__': file_name.replace('_', '.'),
            '__OERPMODULE_MODULE_NAME__': self.name,
            '__OERPMODULE_MODULE_DEVELOPERS__': self.module_developers,
            '__OERPMODULE_MODULE_PLANNERS__': self.module_planners,
            '__OERPMODULE_MODULE_AUDITORS__': self.module_auditors,
        }

        for (var, val) in var_value_dict.iteritems():
            os.system('sed -i \'s/%s/%s/g\' %s' % (var, val, new_file_full_path))
        print ' ----- new.file', new_file_full_path
        return True

    def add_icon_file(self):
        """
        Add the icon.png file to the module.
        """
        print '... Adding module icon'
        this_dir, this_filename = os.path.split(__file__)
        os.system('cp %s/data/icon.png %s/static/src/img/' % (this_dir, self.path))
        return True

    def create_index_html_file(self):
        """
        Touch to create a clean index.html file in the
        static/description/index.html
        """
        print '... Creating a blanck index.html for module description'
        os.system('touch %s/static/description/index.html' % (self.path,))
        return True

    def create_py_files(self, file_py, file_name):
        """
        """
        print '... Create the model and wirzard py files'
        edit_folder = '/'.join([self.path, file_py])
        init_file_full_path = '/'.join([edit_folder, '__init__.py'])
        self.file_name = file_name

        print '... Creating the new file'
#        print 'file_py', file_py
#        print 'file_name', file_name
        self.create_file(
            '.'.join([file_py,'py']),
            '.'.join([file_name, 'py']),
            file_py)

        print '... Add it to the correspond iniy file.'
        os.system('echo """import %s""" >> %s' % (
            file_name, init_file_full_path))
        print ' ----- modified', init_file_full_path
        return True

    def set_license_msg(self, module_developers, module_planners,
                        module_auditors):
        """
        Take the default template for license and add the developers, planners
        and auditors info.
        """

        license_msg = self.template.license_msg

        #~ developer_str = 'Katherine Zaoral <kathy@vauxoo.com>'
        #~ planner_str = 'Humberto Arocha <hbto@vauxoo.com>'
        #~ auditor_str = 'Humberto Arocha <hbto@vauxoo.com>'

        return license_msg % (
            module_developers, module_planners, module_auditors)

    def update_path(self, branch_obj):
        """
        Update the module path using the new branch created.
        @param branch_obj: Branch instance.
        @return: True
        """
        self.path = branch_obj.module.path
        print ' ----- Updating the module path', self.path
        return True

    def create(self):
        """
        This method create a new module, This implies create the main
        directory, create the intern module directories and add the basic files
        like the module descriptor, the init files and the module icon.
        @return True
        """
        self.create_main_directory()
        self.create_directories()
        self.create_base_files()
        return True
