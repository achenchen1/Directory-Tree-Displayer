#!/usr/bin/env python
from colletions import deque
from pathlib import Path
import os
import pathlib
import sys

class Directory:
    def __init__(self, path=None, strict_case=False):
        self.directory = path
        self.strict_case = strict_case
        self.path = self.check_path(path)

    def check_path(self, path):
        # If we're on, in my case, a Mac, Python doesn't recognize the tilde expansion.
        path = os.path.expanduser(path)
        if os.path.exists(path):
            return path
        else:
            print("Path does not exist. Defaulting to root of computer.") if path else pass
            return self.goto_root()

    def goto_root(self):
        current = pathlib.Path(os.getcwd())
        if current == current.parent:
            return current
        else:
            while current.parent != current:
                current = current.parent
            return current

class DirectorySearcher(DirectoryTraverser): 
    def __init__(self, target, path=None, strict_case=False):
        Directory.__init__(self, path, strict_case)
        self.target = target

    def find_all(self, current=None, results=[]):
        if not current:
            current = self.path
        
        # TODO - if target is more than one layer, can we still find it?
        current_items = os.listdir(current)
        for item in current_items:
            if Path(item) == Path(self.target):
                results.append(os.path.abspath(Path(item)))
            if 

        

def help():
    print('''
Directory Explorer by Alex Chen
Accepts relative paths, absolute paths (relative paths take priority), and all arguments and options are case insensitive.

    Arguments:
        --d
            Displays directories and files in current directory. Display depth can be configured with options (see below). 
            If --path is specified, displays under path instead, essentially the same as going into the directory specified with --path, calling display, and then coming back to current working directory.
        
        --s [file or directory name]
            Searches directories for all occurences of specified file. Search depth can be configured with options (see below).
            In the future: implement regex support for this.

        --f [file or directory name]
            Similar to --s, but will return only the first found occurence. Typically finds the \'shallowest\' result. 
    
    Options:
        --path [path] 
            Specifies which directory to execute under. Default is current directory.
        
        --strict-case
            Will perform case-sensitive Search.
''')


if __name__ == '__main__':
    test = {'help': help} # To add: display, search, etc.
    args = sys.argv[2:]
    try:
        test[sys.argv[1]](*args)
    except (ValueError, TypeError):
        help()
