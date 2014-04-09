README
======

Install
-------

Open your command line promt and go to the downloaded package folder to run
this command::

    # sudo python setup.py install

Now check that the package was correctly installed by running this command that
will display the script options::

    $ oerpmodule --help
    Valid actions over a module than can be done with oerpmodule.
      
    {create,branch,append,config}
                          subcommands help
      create              Inicializate module. Create new directory with basic
                          files.
      branch              Create a new module using a branch.
      append              Append a file to the module.
      config              Set and check the oerpmodule config

    Openerp Developer Comunity Tool Development by Vauxoo Team (lp:~vauxoo)
    Coded by Katherine Zaoral <kathy@vauxoo.com>.
    Source code at lp:vauxoo-private/oerpmodule.

Configure
---------

First, need to configure your repositories local paths.
Second, your launchapad-id and acronym for vauxoo-branches.

Actions
-------

To run the installed script just type the command `oerpmodule` and it will show
you what are avaible actions and the required parameters. For more detail
information you can write in your console::

    $ oerpmodule --help
    $ oerpmodule <action> --help

To create a new module directory with its basic structure you need to go to the
directory you want (usually youre branch directory) and run::

    $ oerpmodule create <module_name> -d "Developer <developer@email.com>" \
    > -p "Planner <planner@email.com>" -t "Auditor <auditor@email.com>"

To add a model or wizard file go inside youre module directory and run::

    $ oerpmodule append <module_name> <file_type> <file_name> \
    > -d "Developer <developer@email.com>" -p "Planner <planner@email.com>" \
    > -t "Auditor <auditor@email.com>"

Uninstall
---------

To Uninstall the module you need to re install the module and use the --record
option save the installed files in a new txt file. Like this::
    
    $ sudo python setup.py install --record unistall-files.txt

Then you need to manually remove all the installed files. For this task you
cant use the next command::

    $ sudo su
    # cd <oerpmodule-python-install-folder>
    # cat unistall-files.txt | xargs rm -rf
    # exit
    $ rm unistall-files.txt
