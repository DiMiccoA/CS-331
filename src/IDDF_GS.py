#########################################################################
#Iterative Depth First Search											#
#Created by: Antonio DiMicco and Patrick Oliver							#
#Assignment #1															#
#Works and tested with Python 2.6.6										#
#########################################################################

import gc
from node import Node

def expand(parent, limit):
	#Given a parent node, find valid moves and returns an array of nodes
	index = parent.get_state().index('0')
	expansions = []
	
	#Create possible moves that can happen
	up = index-3
	down = index+3
	left = index-1
	right = index+1

	if up >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), up, index), 
							parent.get_depth()+1, None))
	if index%3+1 <= 2:
		expansions.append(Node(parent, swap(parent.get_state(), right, index), 
							parent.get_depth()+1, None))
	if down < 9:
		expansions.append(Node(parent, swap(parent.get_state(), down, index), 
							parent.get_depth()+1, None))
	if index%3-1 >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), left, index), 
							parent.get_depth()+1, None))

	return expansions
	
def swap(str, a, b):
	#Assumes a valid swap. Swaps elements in a string given positions a and b
	temp = list(str)
	x = temp[a]
	y = temp[b]
	temp[a] = y
	temp[b] = x
	return ''.join(temp)
	
def iterative_depth_first(start, goal):
	limit = 0
	count = 0
	closed = dict()
	fringe = [Node(None, start, 0, None)]
	out = []
	while True:
		while fringe != []:
			temp = fringe.pop(-1)
			if temp.get_state() == goal:
				print "Number of nodes expanded was: ", count, "\n"
				out.append(temp)
				out.append(count)
				return out
			if temp.get_state() in closed:
				if closed[temp.get_state()] == limit:
					continue
			if temp.get_depth() == limit:
				continue
			else:
				expansions = expand(temp, limit)
				fringe.extend(expansions)
				closed[temp.get_state()] = temp.get_depth()
				count += 1
		limit += 1
		gc.collect()
		fringe = [Node(None, start, 0, None)]