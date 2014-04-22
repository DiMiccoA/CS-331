'''
'Node
'Created by: Antonio DiMicco and Patrick Oliver
'Assignment #1
'''

class Node:
	"""Creates a Node that has the parent and state"""
	def __init__(self, parent, state, depth, f_n):
		self.parent = parent
		self.state = state
		self.depth = depth
		self.f_n = f_n
		
	def get_parent(self):
		return self.parent
		
	def get_state(self):
		return self.state
		
	def get_depth(self):
		return self.depth
	
	def get_f_n(self):
		return self.f_n
		
	def set_parent(self, parent):
		self.parent = parent
		
	def set_state(self, state):
		self.state = state
		
	def set_depth(self, depth):
		self.depth = depth
		
	def set_f_n(self, f_n):
		self.f_n = f_n