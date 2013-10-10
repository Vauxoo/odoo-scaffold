README
======

First, need to configure your repositories local paths.
Second, your launchapad-id and acronym for vauxoo-branches.

To run only write::

    ./oerp_module

To usage and option description please typle::

    ./oerp_module --help

To create a new module directory with its basic structure you need to go to the directory you want (usually youre branch directory) and run::

    oerpmodule -cn <module_name> -f . -d "Developer <developer@email.com>" -p "Planner <planner@email.com>" -t "Auditor <auditor@email.com>"

To add a model or wizard file go inside youre module directory and run::

    oerpmodule -n <module_name> -d "Developer <developer@email.com>" -p "Planner <planner@email.com>" -t "Auditor <auditor@email.com>" -a model -f .

