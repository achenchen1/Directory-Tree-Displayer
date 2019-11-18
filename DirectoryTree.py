#!/usr/bin/env python

import sys

class Queue:
    pass
    # To do

class Stack:
    pass
    # To do


def help():
    print('''
Directory Explorer by Alex Chen
Accepts relative paths, and all arguments and options are case insensitive.

    Arguments:
        Display (or 'd')
            Displays directories and files. Display depth can be configured with options (see below). 
        
        Search (or 's') [file name]
            Searches directories for specified file. Search depth can be configured with options (see below).
    
    Options:
        --depth [number >= 0]
            Specifies how deep for the command to go. For example, display my_directory --depth 0 will only 
            search in my_directory, while --depth 0 will search my_directory and one beneath it. Default is
            to go as deep as possible.
        
        --path [path] or --directory
            Specifies which directory to execute under. Default is current directory.
        
        --strict-case
            Will perform case-sensitive Search.
        
    Examples:
        DirectoryTree.py d --depth 0
        (Displays only files and directories in current working directory)
        
        DirectoryTree.py s My_Text_File.txt --path /users/Alice/Documents
        (Looks for all results matching My_Text_File.txt in all subdirectories of /users/Alice/Documents)
''')


if __name__ == '__main__':
    test = {'help': help} # To add: display, search, etc.
    args = sys.argv[2:]
    try:
        test[sys.argv[1]](*args)
    except (ValueError, TypeError):
        help()
