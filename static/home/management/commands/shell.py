from django.core.management.commands.shell import Command as DjangoCommand
from ptpython.repl import embed, run_config
from importlib import import_module
import os


def default_imports():
    # imports listed here are automatically loaded into the shell
    from home import models as hmod
    import json
    import re
    import os, os.path

    # return the variables created here
    return locals()


class Command(DjangoCommand):
    '''Makes `ptpython` the default Django shell'''
    shells = [ 'ptpython' ] + DjangoCommand.shells

    def ptpython(self, options):
        history_filename = os.path.expanduser('~/.ptpython_history')

        # start the interpreter
        globals_dict = default_imports()
        locals_dict = {}
        embed(globals_dict, locals_dict, history_filename=history_filename, configure=run_config)
