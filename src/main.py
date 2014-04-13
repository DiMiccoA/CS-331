'''
Created on Apr 12, 2014

@author: anton_000
'''
import sys
import BF_GS as bfs
from node import Node

def build_state(file):
	state = ''
	fd = open(file, 'r')
	for line in fd:
		line = line.replace(',','').replace('\n','')
		state = state+line
		
	return state

def print_parents(node, outputfd):
	if node is None: #node.get_parent == 0:
		#print_state(node.get_state())
		#output_to_file(outputfd, node.get_state())
		#print '- - -'
		return
	print_parents(node.get_parent(),outputfd)
	print_state(node.get_state())
	output_to_file(outputfd, node.get_state())
	print '- - -'
	return
			
def print_state(state):
	for x in range(0,3):
		print state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]
		
def output_to_file(output,state):
	for x in range(0,3):
		output.write(state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]+'\n')
	output.write('- - -\n')
	
def main(init, final, mode, output):
	sys.setrecursionlimit(500000)
	start = ''
	goal = ''
	start = build_state(init)
	goal = build_state(final)
	outputfd = open(output, 'w')
	
	if mode == 'bfs':
		print_parents(bfs.breadth_first(start, goal), outputfd)
	elif mode == 'dfs':
		pass
	elif mode == 'iddfs':
		pass
	elif mode == 'astar':
		pass
	outputfd.close()

   
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])