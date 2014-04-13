'''
Created on Apr 12, 2014

@author: anton_000
'''

from node import Node

def expand(parent):
	#Given a parent node, find valid moves and returns an array of nodes
	index = parent.state.index('0')
	expansions = []
	
	#Create possible moves that can happen
	up = index-3
	down = index+3
	left = index-1
	right = index+1

	if up >= 0:
		expansions.append(Node(parent, swap(parent.state, up, index)))
	if down < 9:
		expansions.append(Node(parent, swap(parent.state, down, index)))
	if index%3-1 >= 0:
		expansions.append(Node(parent, swap(parent.state, left, index)))
	if index%3+1 <= 2:
		expansions.append(Node(parent, swap(parent.state, right, index)))
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
	count = 0
	closed = []
	fringe = [Node(None, start)]
	while fringe != []:
		temp = fringe.pop()
		if temp.state == goal:
			print "Number of nodes expanded was: ", count, "\n"
			return temp
		if temp.state in closed:
			continue
		else:
			closed.append(temp.state)
			expansions = expand(temp)
			map(fringe.append, expansions)
			count += 1