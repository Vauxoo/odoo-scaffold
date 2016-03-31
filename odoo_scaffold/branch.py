#!/usr/bin/python
import os
from config import Config


class Branch(object):

    """
    Branch representing object.
    """

    def __init__(self, module_obj, branch_suffix, parent_repo, version,
                 folder):
        """
        Initializate branch object
        @param module_name:
        @param branch_suffix:
        @param parent_repo:
        @param version: the version of the new model
        """

        self.config = Config()
        if parent_repo not in self.config.repositories:
            raise Exception(
                "Bad paramenters. The repository %s does not exist"
                " in the current script configuration. Please add"
                " the repo to the repository data." % (parent_repo,))
        if version not in self.config._oerp_version_list:
            raise Exception("Bad parameters. '%s' Its not a valid openerp "
                            "version" % (version,))

        self.module = module_obj
        self.version = version
        self.branch_suffix = branch_suffix or ''
        self.parent_repo = self.config.repositories[parent_repo]

        self.branch_name = '-'.join(
            self.branch_suffix and
            [self.version, self.module.name, 'dev', self.branch_suffix] or
            [self.version, self.module.name, 'dev'])

        self.path = '%s/%s' % (folder, self.branch_name)
        self.module.path = '%s/%s' % (self.path, self.module.name)

        print ' ----- branch.path', self.path
        print ' ----- module.path', self.module.path

        self.repo_name = self.parent_repo.name
        self.repo_group = self.parent_repo.group
        self.repo_gdev = self.parent_repo.gdev
        self.repo_serie = self.parent_repo.serie

    def create_branch(self):
        """
        Create a new branch for the development module using the parent repo
        serie branch like point of start:
        1. create module new local branch by copying the parent local repo
        2. create module new cloud branch by copying the parent cloud repo
        3. link both local and cloud branches
        4. mark new branch with a init revision for new module
        """
        # TODO update parent repo before copy for the new module

        print '... Creating branch for the new module'
        print ' ----- [Note]: This process can take a while. Please wait...'

        src_cloud_branch_name = '/'.join(
            self.repo_serie and
            [self.repo_group, self.repo_name, self.repo_serie] or
            [self.repo_group, self.repo_name])
        new_cloud_branch_name = '/'.join(
            [self.repo_group, self.repo_name, self.branch_name])

        print ' ----- src.cloud.branch', src_cloud_branch_name
        print ' ----- new.cloud.branch', new_cloud_branch_name
        print ' ----- new.local.branch', self.path

        print '... Create new local branch'
        os.system(
            'cp %s %s -r' % (self.parent_repo.local_path, self.path))

        print '... Create new cloud branch'
        os.system(
            'cd %s && git checkout -b %s --track %s/%s --quiet' %
            (self.path, self.branch_name, self.repo_group, self.repo_serie,)
        )

        print '... Linking local and cloud branchs'
        os.system(
            'cd %s && git pull %s %s --quiet' %
            (self.path, self.repo_group, self.repo_serie)
        )

        return True

    # TODO: this method is not used yet. please test.
    def branch_changes_apply(self):
        """
        Create one revision to commit the structure and basic module files
        after the creation from scratch.
        """

        print '... Commit the module init of structure and basic files'
        os.system(
            'cd %s && git add . && git commit -m "%s" --quiet' %
            (self.path, '[ADD] %s: Module structure and basic files' %
             (self.module.name)))
        return True

    # TODO: this method is not used yet. please test.
    def push_changes(self):
        """
        Push changes of the parent at the cloud
        """
        print '... Push changes to branch at cloud'
        os.system(
            'cd %s && git push %s %s --quiet' %
            (self.path, self.repo_gdev, self.branch_name))
        return True
