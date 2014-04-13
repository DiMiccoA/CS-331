"""
Node
Created by: Antonio DiMicco and Patrick Oliver
Class: CS331
"""

class Node:
	"""Creates a Node that has the parent and state"""
	def __init__(self, parent, state):
		self.parent = parent
		self.state = state
		
	def get_parent(self):
		return self.parent
		
	def get_state(self):
		return self.state
		
	def set_parent(self, parent):
		self.parent = parent
		
	def set_state(self, state):
		self.state = state