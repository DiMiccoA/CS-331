#########################################################################
#main																	#
#Created by: Antonio DiMicco and Patrick Oliver							#
#Assignment #1															#
#Takes 4 command line arguments: 										#
#<initial state txt file> <goal state txt file> <mode> <output file>	#
#Run the program as such: python <initial> <goal> <mode> <output>		#
#Works and tested with Python 2.6.6										#
#########################################################################

import sys
import BF_GS as bfs
import DF_GS as dfs
import IDDF_GS as iddfs
import ASTAR as astar
from node import Node

def build_state(file):
	state = ''
	fd = open(file, 'r')
	for line in fd:
		line = line.replace(',','').replace('\n','')
		state = state+line
		
	return state

def print_parents(node, outputfd):
	states = []
	moves = 0
	while node is not None:
		states.append(node.get_state())
		node = node.get_parent()
		moves += 1
	
	for state in reversed(states):
		print_state(state)
		output_to_file(outputfd, state)
		
	moves -= 1 #Subtracts the start node, which isn't a move
	print 'Number of moves taken to find the goal was: ', moves
	outputfd.write('Number of moves taken to find the goal was: '+str(moves)+'\n')
	
			
def print_state(state):
	for x in range(0,3):
		print state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]
	print '- - -'
		
def output_to_file(output,state):
	for x in range(0,3):
		output.write(state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]+'\n')
	output.write('- - -\n')
	
def main(init, final, mode, output):
	start = ''
	goal = ''
	start = build_state(init)
	goal = build_state(final)
	outputfd = open(output, 'w')
	output = []
	
	if mode == 'bfs':
		output = bfs.breadth_first(start, goal)
		print_parents(output[0], outputfd)
		print "Number of nodes expanded was: ", output[1], "\n"
		outputfd.write("Number of nodes expanded was: "+str(output[1])+"\n")
	elif mode == 'dfs':
		output = dfs.depth_first(start, goal)
		print_parents(output[0], outputfd)
		print "Number of nodes expanded was: ", output[1], "\n"
		outputfd.write("Number of nodes expanded was: "+str(output[1])+"\n")
	elif mode == 'iddfs':
		output = iddfs.iterative_depth_first(start, goal)
		print_parents(output[0], outputfd)
		print "Number of nodes expanded was: ", output[1], "\n"
		outputfd.write("Number of nodes expanded was: "+str(output[1])+"\n")
	elif mode == 'astar':
		output = astar.astar(start, goal)
		print_parents(output[0], outputfd)
		print "Number of nodes expanded was: ", output[1], "\n"
		outputfd.write("Number of nodes expanded was: "+str(output[1])+"\n")
		
	outputfd.close()

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])