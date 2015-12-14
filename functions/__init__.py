# The purpose of making an __init__.py is that this file makes this folder a python directory, so that it can be
# used in import statements.
# for eg. 'from functions import basic_arguments' or 'import functions.basic_arguments'
# The other use is to override the __all__ in-built variable. It is the list of classes/functions/variables which
# will be exposed when a 'import *' is used with this python directory

from basic_arguments import *
__all__ = [add_to_list, add_prefix, add, display_employee, sample_function]
