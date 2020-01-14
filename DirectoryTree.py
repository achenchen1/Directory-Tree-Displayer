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
			return self._goto_root()

	def _goto_root(self):
		# In the future, maybe consider a binary search. But it looks like for a binary search, we'd be looking at errors, which are expensive to handle.
		current = pathlib.Path(os.getcwd())
		while current.parent != current:
			current = current.parent
		return current

class DirectorySearcher(DirectoryTraverser): 
	def __init__(self, target, path=None, strict_case=False):
		Directory.__init__(self, path, strict_case)
		self.results = []
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
		if not current.suffix:
			extension = False
		else:
			extension = True

		if self.target != self.target.name:
			# TODO: does 'expanding', i.e. going to parents[1], parents[2], parents[4], parents[8], like a binary search, go faster? It should be O(log n)... right? 
			#		as opposed to just iterating 1 by 1
			self._r_find_all_path(current, extension)
		else:
			self._r_find_all_name(current, extension)
			# Base name is the same, but is the rest of it same?
			# Also - do .lnks, junctions, symbolic links etc. work fine?
		results = self.results
		self.results = []
		return results
	
	# TODO: Handle file extensions. 'test.py' exists, 'test' does not.
	def _r_find_all_path(self, current):
		for item in current.iterdir():
			if item.joinpath(self.target).exists:
				# TODO: is there ever a scenario where we're looking for a/b/, and there's a/b/a/b/a/b?
				self.results.append(item.joinpath(self.target))
			if item.is_dir():
				self._r_find_all_path(item)
		return None

	def _r_find_all_name(self, current):
		for item in current.iterdir():
			if item == self.target:
				self.results.append(item)
			if item.is_dir():
				self._r_find_all_name(item)
		return None
				

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

