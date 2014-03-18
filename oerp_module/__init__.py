import module
import config
import branch 
from module import Module
from config import Config
from branch import Branch 

def run(args, config):
    """
    run the corresponding action
    """
    if args.action == 'config':
        args.list_repositories and config.print_repositories()
    else:
        module = Module(
            args.module_name, args.module_developers, args.module_planners,
            args.module_auditors, folder=args.destination_folder)

        if args.action == 'branch':
            branch = Branch(
                module, args.branch_suffix, args.parent_repo,
                args.oerp_version, args.destination_folder)
            branch.create_branch()
            module.update_path(branch)
            module.create_main_directory()
            module.create_directories()
            module.create_base_files()
        elif args.action == 'create':
            module.create_main_directory()
            module.create_directories()
            module.create_base_files()

        elif args.action == 'append':
            module.create_py_files(args.append_file, args.file_name)

        #~ module.branch_changes_apply()
    return True

def confirm_run(args):
    """
    Manual confirmation before runing the script. Very usefull.
    """
    print'\n... Configuration of Parameters Set'
    for (parameter, value) in args.__dict__.iteritems():
        print '%s = %s' % (parameter, value)

    confirm_flag = False
    while confirm_flag not in ['y', 'n']:
        confirm_flag = raw_input(
            'Confirm the run with the above parameters? [y/n]: ')
        if confirm_flag == 'y':
            print 'The script parameters were confirmed by the user'
        elif confirm_flag == 'n':
            print 'The user cancel the operation'
            exit()
        else:
            print 'The entry is not valid, please enter y or n.'
    return True

def main():

    config = Config()
    args = config.argument_parser()
    confirm_run(args)
    run(args, config)

