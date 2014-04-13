'''
Created on Apr 12, 2014

@author: anton_000
'''
import sys
import BF_GS as bfs
from node import Node

def build_state(file):
	#Builds a 2D array given a file
	#arr = []
	#fd = open(file, 'r')
	#for line in fd:
	#	arr.append(line.strip().split(','))
	state = ''
	fd = open(file, 'r')
	for line in fd:
		line = line.replace(',','').replace('\n','')
		state = state+line
		
	return state
	#return arr
		
	
def print_double_array(arr):
	#Prints a double array all pretty like.
	for element in arr:
		for row in element:
			print('\t'.join(row))

def print_parents(node):
	if node.parent == None:
		print_state(node.state)
		print '- - -'
		return
	print_parents(node.parent)
	print_state(node.state)
	print '- - -'
	return
	
			
def print_state(state):
	for x in range(0,3):
		print state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]+'\n'
		
def main():
	start = ''
	goal = ''
	start = build_state('testStart2.txt')
	goal = build_state('testGoal2.txt')

	print_parents(bfs.breadth_first(start, goal))

   
if __name__ == '__main__':
	main()