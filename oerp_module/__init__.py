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
