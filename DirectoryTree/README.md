

- tree.py provides an entry-point script for you to run the application.

- Then you have the rptree/ directory that holds a Python package with three modules:

rptree.py provides the application’s main functionalities.
__init__.py enables rptree/ as a Python package.
cli.py provides the command-line interface for the application.

- Your directory tree generator tool will run on the command line. It’ll take arguments, process them, and display a directory tree diagram on the terminal window. It can also save the output diagram to a file in markdown format.

- To run the first step, you need to provide a way for your application to take a directory path at the command line. To do this, you’ll use Python’s argparse module from the standard library.
 - To complete the second and third steps, you’ll use pathlib. This module provides several tools to manage and represent file system paths. Finally, you’ll use a regular Python list to store the list of entries in the directory structure.
