README
======

This module python is a tool to Odoo developers that permit to generate a
new Odoo modules from the command line indicating only a few arguments. Some
features are:

 - Create a new Odoo module structure and basic files.
 - Let to add initial data to a new module (using csv2xml) for company data
   initilization Odoo modules.
 - Let to expand a customize easly your Odoo module by append new models and
   wizard files.
 - Permit create the Odoo module inside an existing github branch. This
   way you can add youre new module easly to a Odoo addons repository
   automactly.

This is a practical way to work with a client. The client can create a new
Odoo module to be developed by running this tool time saver and also
reduce in a big way the human errors.

Download
--------

This python module is hosted on github repository branch. Can be
downloaded by running this command::
    
    git clone git@github.com:Vauxoo/odoo-scaffold.git

Dependencies
------------

This module python use some imports of python modules, some of then really
commom and another need to be found, downloaded and then installed via apt-get
install or pip, if not, then you need to search in the web for the official
page of the module, download the module and install it with the installation
instruction given for the module autor. The list of used python modules until
the last versions is this: ``os``, ``argparse``, ``pprint``, ``sys``,
``argcomplete``, and ``csv2xml``.

.. note:: the csv2xml python module is a special module, you can get a copy by
   runing this consola command::

        git clone git@github.com:Vauxoo/csv2xml.git

Install
-------

Open your command line promt and go to the downloaded package folder to run
this command::

    # sudo python setup.py install

Now check that the package was correctly installed by running this command that
will display the script options::

    $ odooscaffold --help
    Valid actions over a module than can be done with oerpmodule.
      
    {create,branch,append,config}
                          subcommands help
      create              Inicializate module. Create new directory with basic
                          files.
      branch              Create a new module using a branch.
      append              Append a file to the module.
      config              Set and check the odooscaffold config

    Odoo Developer Comunity Tool Development by Vauxoo Team (https://github.com/vauxoo)
    Coded by Katherine Zaoral <kathy@vauxoo.com>.
    Source code at git@github.com:Vauxoo/odoo-scaffold.git

Configure
---------

If you try to use the odooscaffold you will get errors because first you need to
configure some info about the repositories and github Go to config.py file
and you will find a list of repositories. You need to set the correct data for
your computer to make the correct link to use the branchs functionality.

Vauxoo developer also dont forget to set your acronym vauxoo nick name used to
set your registred branches suffix (to identificate that that branch of the
vauxoo teams is yours).

Actions
-------

To run the installed script just type the command `oerpmodule` and it will show
you what are avaible actions and the required parameters. For more detail
information you can write in your console::

    $ odooscaffold --help
    $ odooscaffold <action> --help

To create a new module directory with its basic structure you need to go to the
directory you want (usually youre branch directory) and run::

    $ odooscaffold create <module_name> -d "Developer <developer@email.com>" \
    > -p "Planner <planner@email.com>" -t "Auditor <auditor@email.com>"

To add a model or wizard file go inside youre module directory and run::

    $ odooscaffold append <module_name> <file_type> <file_name> \
    > -d "Developer <developer@email.com>" -p "Planner <planner@email.com>" \
    > -t "Auditor <auditor@email.com>"

Documentation
-------------

The detail documentation about this tool can be found inside the vauxoo
documentation branch in the section CSV Tools.

Uninstall
---------

In the install folder there is a uninstall file. This is an executable file.
Just run in your console::

    $ sudo ./uninstall

If the file have not excecution permissions then just change the file
permissions (chmod) and execute the above command.
