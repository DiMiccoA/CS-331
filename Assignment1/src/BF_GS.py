#########################################################################
#Breadth First Search													#
#Created by: Antonio DiMicco and Patrick Oliver							#
#Assignment #1															#
#Works and tested with Python 2.6.6										#
#########################################################################

from node import Node

def expand(parent):
	#Given a parent node, find valid moves and returns an array of nodes
	index = parent.get_state().index('0')
	expansions = []
	
	#Create possible moves that can happen
	up = index-3
	down = index+3
	left = index-1
	right = index+1

	if up >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), up, index), None, None))
	if index%3+1 <= 2:
		expansions.append(Node(parent, swap(parent.get_state(), right, index), None, None))
	if down < 9:
		expansions.append(Node(parent, swap(parent.get_state(), down, index), None, None))
	if index%3-1 >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), left, index), None, None))

	return expansions
	
def swap(str, a, b):
	#Assumes a valid swap. Swaps elements in a string given positions a and b
	temp = list(str)
	x = temp[a]
	y = temp[b]
	temp[a] = y
	temp[b] = x
	return ''.join(temp)
	
def breadth_first(start, goal):
	closed = dict()
	fringe = [Node(None, start, None, None)]
	out = []
	while fringe != []:
		temp = fringe.pop(0)
		if temp.get_state() == goal:
			print "Number of nodes expanded was: ", len(closed), "\n"
			out.append(temp)
			out.append(len(closed))
			return out
		if temp.get_state() in closed:
			continue
		else:
			closed[temp.get_state()] = True
			expansions = expand(temp)
			fringe.extend(expansions)