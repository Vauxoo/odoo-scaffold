#!/usr/bin/python
import os
import sys
from config import *


class Template(object):

    """
    Contains the files templates
    """

    license_msg = \
"""#!/usr/bin/python
# -*- encoding: utf-8 -*-
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://www.vauxoo.com>).
#    All Rights Reserved
############# Credits #########################################################
#    Coded by: %s
#    Planified by: %s
#    Audited by: %s
###############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""

    model_py = \
"""
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
from openerp import tools


class %s(osv.Model):
    '''
    Need to set the model description
    '''

    _name = '%s'
    _description = 'Need to set the model name'
    _columns = {
        'name': fields.char(
            'Name',
            required=True,
            size=64,
            help='help string'),
    }

    _defaults = {
    }
"""

    wizard_py = \
"""
from openerp.osv import osv, fields
from openerp.tools.translate import _
import decimal_precision as dp


class %s_wizard(osv.osv_memory):
    '''
    Need to set the model description
    '''
    _name = '%s'
    _description = 'Need to set the model name'

    _columns = {
    }

    _defaults = {
    }

"""

    openerp_py = \
"""
{
    'name': '%s',
    'version': '1.0',
    'author': 'Vauxoo',
    'website': 'http://www.vauxoo.com/',
    'category': '',
    'description': '''
''',
    'depends': [],
    'data': [],
    'demo': [],
    'test': [],
    'qweb': [],
    'js': [],
    'css': [],
    'active': False,
    'installable': True,
}"""


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
        self.name = name
        self.directory = name
        self.path = '%s/%s' % (folder, self.directory)

        self.template = Template()
        self.license_msg = self.set_license_msg(module_developers,
                                                module_planners,
                                                module_auditors)
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
        init_files = {
            '__init__.py': 'import model\nimport wizard',
            'model/__init__.py': '',
            'wizard/__init__.py': '',
        }

        print '... Creating init files'
        for (new_file, content) in init_files.iteritems():
            os.system('echo """%s""" | cat - > %s' % (
                self.license_msg + content, '%s/%s' % (self.path, new_file)))
        return True

    def create_openerp_file(self):
        """
        Create the openerp descriptive file
        """
        content = self.template.openerp_py % (self.name,)

        print '... Create the openerp descriptive file'
        os.system('echo """%s""" | cat - > %s' % (
            self.license_msg + content, '%s/__openerp__.py' % (self.path,)))
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
        new_file_full_path = '/'.join([edit_folder, '.'.join([file_name, 'py'])])

        content = self.license_msg + getattr(
            self.template, file_py + '_py') % (
                file_name, file_name.replace('_', '.'))

        print '... Creating the new file'
        os.system('echo """%s""" | cat - > %s' % (
            content, new_file_full_path))
        print ' ---- new file', new_file_full_path

        print '... Add it to the correspond iniy file.'
        os.system('echo """import %s""" >> %s' % (
            file_name, init_file_full_path))
        print ' ---- modificated file', init_file_full_path
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
