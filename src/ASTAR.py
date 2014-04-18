#########################################################################
#Iterative Depth First Search											#
#Created by: Antonio DiMicco and Patrick Oliver							#
#Assignment #1															#
#Works and tested with Python 2.6.6										#
#########################################################################

import gc
from node import Node

def expand(parent, goal):
	#Given a parent node, find valid moves and returns an array of nodes
	index = parent.get_state().index('0')
	expansions = []
	
	#Create possible moves that can happen
	up = index-3
	down = index+3
	left = index-1
	right = index+1
	
	current_depth = parent.get_depth()+1
	if up >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), up, index), 
					current_depth, current_depth+h(parent.get_state(),goal)))
	if index%3+1 <= 2:
		expansions.append(Node(parent, swap(parent.get_state(), right, index), 
					current_depth, current_depth+h(parent.get_state(),goal)))
	if down < 9:
		expansions.append(Node(parent, swap(parent.get_state(), down, index), 
					current_depth, current_depth+h(parent.get_state(),goal)))
	if index%3-1 >= 0:
		expansions.append(Node(parent, swap(parent.get_state(), left, index), 
					current_depth, current_depth+h(parent.get_state(),goal)))

	return expansions
	
def swap(str, a, b):
	#Assumes a valid swap. Swaps elements in a string given positions a and b
	temp = list(str)
	x = temp[a]
	y = temp[b]
	temp[a] = y
	temp[b] = x
	return ''.join(temp)

def h(state, goal):
		sum = 0
		for current_state_index in range(0, len(state)):
			final_state_index = goal.find(goal[current_state_index])
			sum += (abs(current_state_index%3 - final_state_index) + 
						abs(current_state_index - final_state_index))
		return sum
			
def astar(start, goal):
	depth = 0
	count = 0
	closed = dict()
	fringe = [Node(None, start, 0, 0+h(start, goal))]
	temp = None
	out = []
	while fringe != []:
		temp = fringe.pop(0)
		if temp.get_state() == goal:
			print "Number of nodes expanded was: ", count, "\n"
			out.append(temp)
			out.append(count)
			return out
		if temp.get_state() in closed:
			if closed[temp.get_state()] < temp.get_f_n():
				continue
			else:
				fringe.extend(expand(temp, goal))
				fringe.sort(key = lambda node: node.f_n)
				closed[temp.get_state()] = temp.get_f_n()
				count+=1
		else:
			expansions = expand(temp, goal)
			fringe.extend(expansions)
			fringe.sort(key = lambda node: node.f_n)
			closed[temp.get_state()] = temp.get_f_n()
			count += 1