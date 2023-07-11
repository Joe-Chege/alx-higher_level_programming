#!/usr/bin/python3

""" A class that inherits from list"""


class MyList(list):
	"""implements sorted printing """
	
	def print_sorted(self):
		"""prints list, but sorted in ascending sort"""
		print(sorted(self))
