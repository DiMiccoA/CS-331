'''
Created on Apr 12, 2014

@author: anton_000
'''

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
	
def print_state(state):
	for x in range(0,3):
		print state[x*3]+' '+state[x*3+1]+' '+state[x*3+2]+'\n'
		
def main():
	start = ''
	goal = ''
	start = build_state('testStart1.txt')
	print_state(start)
	goal = build_state('testGoal1.txt')
	print '\n'
	print_state(goal)

#	start = []
#	goal = []
#	start.append(build_array('testStart1.txt'))
#	goal.append(build_array('testGoal1.txt'))
#	print 'start config:'
#	print_double_array(start)
#	print '\ngoal config:'
#	print_double_array(goal)
   
if __name__ == '__main__':
	main()