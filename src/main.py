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
	while node is not None:
		states.append(node.get_state())
		node = node.get_parent()
	
	for state in reversed(states):
		print_state(state)
		output_to_file(outputfd, state)
	
			
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
	
	if mode == 'bfs':
		print_parents(bfs.breadth_first(start, goal), outputfd)
	elif mode == 'dfs':
		print_parents(dfs.depth_first(start, goal), outputfd)
	elif mode == 'iddfs':
		print_parents(iddfs.iterative_depth_first(start, goal), outputfd)
	elif mode == 'astar':
		print_parents(astar.astar(start, goal), outputfd)
	outputfd.close()

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])