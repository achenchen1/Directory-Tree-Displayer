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
		try:
			self.target = Path(target)
		except TypeError:
			print("Unexpected type. Expecting string or similar type.")

	def find_all(self, current=None):
		"""
		Traverses through entire directory tree by using Depth First Search, and appends all found results.

		Should basically accomplish the same functionality as pathlib.Path().glob
		"""	
		current = self.path
		# TODO: remember pathlib.Path.iterdir is a thing, and can be used instead of an array
				   
		if self.target != self.target.name:
			# TODO: does 'expanding', i.e. going to parents[1], parents[2], parents[4], parents[8], like a binary search, go faster? It should be O(log n)... right? 
			#		as opposed to just doing a while loop
			path_args = deque()
			path_args.appendleft(self.target.name)
			try:
				while # is there an alternative to while True that works here?:
					
			
			return self._r_path_find_all(current, [])
		else:
			return self._r_name_find_all(current, [])
			# Base name is the same, but is the rest of it same?
			# Also - do .lnks, junctions, symbolic links etc. work fine?

				

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

