'''
Created on Apr 12, 2014

@author: anton_000
'''

from node import Node

def expand(parent):
	#ToDo: Implement Expand
	pass
	
def breadth_first(start, goal):
	count = 0
	closed = []
	fringe = [node(0, start)]
	while fringe != []:
		temp = fringe.pop()
		if temp.state == goal:
			print "Number of nodes expanded was: " + count
			return temp
		if temp.state in closed:
			continue
		else:
			closed.append(temp.state)
			fringe.append(expand(temp.state))
			count += 1