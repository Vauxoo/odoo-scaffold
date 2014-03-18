#!/usr/bin/python
import os
import pprint
import argparse
import argcomplete


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
        self._oerp_version_list = ['6.0', '6.1', '7.0']
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
    def argument_parser(self):
        """
        This function create the help command line and manage and filter the
        parameters of this program (default values, choices values)
        """
        parser = argparse.ArgumentParser(
            prog='oerpmodule',
            description='Create new openerp module structure and basic files.',
            epilog="""
Openerp Developer Comunity Tool
Development by Vauxoo Team (lp:~vauxoo)
Coded by Katherine Zaoral <kathy@vauxoo.com>.
Source code at lp:~katherine-zaoral-7/+junk/oerp_module.""",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        subparsers = parser.add_subparsers(
            description=('Valid actions over a module than can be done with'
                ' oerpmodule.'),
            dest='action',
            help='subcommands help')

        # create sub parser for create action
        create_parser = subparsers.add_parser(
            'create',
            help='Inicializate module. Create new directory with basic files.')
        create_paser = self.add_common_options(create_parser)

        # create sub parser for branch action
        branch_parser = subparsers.add_parser(
            'branch',
            help='Create a new module using a branch.')
        branch_paser = self.add_common_options(branch_parser)

        branch_parser.add_argument(
            '-r', '--parent_repo',
            metavar='PARENT_REPO',
            type=str,
            required=True,
            choices=self.get_repositories_names(),
            help=('The name of repository from will be create the new module. To '
                  'look the repository list use oerpmodule config -l.'))

        branch_group = branch_parser.add_argument_group('New Branch Name options', (
            'This way you can configure the new branch name.'))

        branch_group.add_argument(
            '-s', '--branch-suffix',
            metavar='DEVELOPER_ACRONYM',
            type=str,
            help=str('Generally developer acronym name. It use when creating the'
                     ' branch for identify the team user owner in a simply way,'
                     ' It use is recommended.'))
        branch_group.add_argument(
            '-ov', '--oerp-version',
            metavar='VERSION',
            type=str,
            choices=self._oerp_version_list,
            help='Openerp version number')

        branch_parser.set_defaults(
            oerp_version='7.0',
            parent_repo='addons-vauxoo')

        # create sub parser for append action
        append_parser = subparsers.add_parser(
            'append', 
            help='Append a file to the module.')
        append_paser = self.add_common_options(append_parser)

        append_parser.add_argument(
            'append_file',
            metavar='FILE_TYPE',
            type=str,
            choices=['model', 'wizard'],
            help='The type of file you want to append.')
        append_parser.add_argument(
            'file_name',
            metavar='FILE_NAME',
            type=str,
            help='the name of the new model or wizard file that will be created.')

        # create sub parser for config action
        config_parser = subparsers.add_parser(
            'config', 
            help='Set and check the oerpmodule config')
        config_parser.add_argument(
            '-l', '--list-repositories', action='store_true',
            help='List the configurate repositories.')

        argcomplete.autocomplete(parser)
        return parser.parse_args()

    def add_common_options(self, subparser):
        """
        I recive a parser object that repersent a subparser in this script to add
        it the common options needed. The subparser that share this common options
        are [create, append, branch] subparsers. The common options are:
        [module_name, module_developers, module_planners, module_auditors, dir].
        @return: the subparser object with the common arguments added.
        """
        subparser.add_argument(
            'module_name',
            metavar='MODULE_NAME',
            type=str,
            help='name of the module to create.')
        subparser.add_argument(
            '-d', '--module-developers',
            metavar='DEVELOPERS_INFO',
            type=str,
            help=str('A string with the module developers information. The format'
                     ' of this string is \'First Developer Name'
                     ' <developer@mail.com>, Second Developer Name'
                     ' <developerX@mail.com>\''),
            required=True)
        subparser.add_argument(
            '-p', '--module-planners',
            metavar='PLANNERS_INFO',
            type=str,
            help=str('A string with the module planners information. The format'
                     ' of this string is \'First Planner Name'
                     ' <planner@mail.com>, Second Planner Name'
                     ' <plannerX@mail.com>\''),
            required=True)
        subparser.add_argument(
            '-t', '--module-auditors',
            metavar='AUDITORS_INFO',
            type=str,
            help=str('A string with the module auditors information. The format'
                     ' of this string is \'First Auditor Name'
                     ' <auditor@mail.com>, Second Auditor Name'
                     ' <auditorX@mail.com>\''),
            required=True)
        subparser.add_argument(
            '-dir', '--destination-folder',
            metavar='DIR',
            type=str,
            default=os.getcwd(),
            help='name of the folder where to put the module')
        return subparser
