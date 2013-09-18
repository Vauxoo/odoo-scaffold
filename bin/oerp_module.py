#!/usr/bin/python
import argparse

def argument_parser():
    """
    This function create the help command line and manage and filter the
    parameters of this program (default values, choices values)
    """
    parser = argparse.ArgumentParser(
        prog='new_module_openerp',
        description='Create new openerp module structure and basic files.',
        epilog="""
Openerp Developer Comunity Tool
Development by Vauxoo Team (lp:~vauxoo)
Coded by Katherine Zaoral <kathy@vauxoo.com>.
Source code at lp:~katherine-zaoral-7/+junk/oerp_module.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'name',
        metavar='MODULE_NAME',
        type=str,
        help='name of the module to create.')
    parser.add_argument(
        '-s', '--branch-suffix',
        metavar='DEVELOPER_ACRONYM',
        type=str,
        help=str('branch suffix. Generally developer acronym name. It use when'
                 ' creating the branch for identify the team user owner in a'
                 ' simply way'),
        required=True)
    parser.add_argument(
        '-r', '--parent_repo',
        metavar='PARENT_REPO',
        type=str,
        help='name of parent repo',
        choices=repo_data.keys())
    parser.add_argument(
        '-ov', '--oerp-version',
        metavar='VERSION',
        type=str,
        choices=_oerp_version_list,
        help='Openerp version number')
    parser.add_argument(
        '-c', '--create-structure', action='store_true',
        help='inicializate module / create new directory with basic files')
    parser.add_argument(
        '-b', '--branch-create', action='store_true',
        help='create a branch copy in the parent repo that will holds the new'
             ' module')
    parser.add_argument(
        '-a', '--append-file',
        metavar='TYPE_OF_FILE',
        type=str,
        help='append a file to the module',
        choices=['model', 'wizard'])
    parser.add_argument(
        '-d', '--module-developers',
        metavar='DEVELOPERS INFO',
        type=str,
        help=str('A string with the module developers information. The format'
                 ' of this string is \'First Developer Name'
                 ' <developer@mail.com>, Second Developer Name'
                 ' <developerX@mail.com>\''),
        required=True)
    parser.add_argument(
        '-p', '--module-planners',
        metavar='PLANNERS INFO',
        type=str,
        help=str('A string with the module planners information. The format'
                 ' of this string is \'First Planner Name'
                 ' <planner@mail.com>, Second Planner Name'
                 ' <plannerX@mail.com>\''),
        required=True)
    parser.add_argument(
        '-t', '--module-auditors',
        metavar='AUDITORS INFO',
        type=str,
        help=str('A string with the module auditors information. The format'
                 ' of this string is \'First Auditor Name'
                 ' <auditor@mail.com>, Second Auditor Name'
                 ' <auditorX@mail.com>\''),
        required=True)

    parser.set_defaults(
        oerp_version='7.0',
        parent_repo='addons-vauxoo'
    )

    return parser.parse_args()

def main():

    args = argument_parser()

    print'\n... Configuration of Parameters Set'
    for (parameter, value) in args.__dict__.iteritems():
        print '%s = %s' % (parameter, value)

    module = oerp_module(
        args.name, args.branch_suffix, args.parent_repo, args.oerp_version,
        args.module_developers, args.module_planners, args.module_auditors)

    if args.branch_create:
        module.create_branch()

    if args.create_structure:
        module.create_main_directory()
        module.create_directories()
        module.create_base_files()

    if args.append_file:
        module.create_py_files(args.append_file)

        #~ module.branch_changes_apply()

if __name__ == '__main__':
    main()
