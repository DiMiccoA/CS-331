'''
Created on Apr 12, 2014

@author: anton_000
'''

def build_array(file):
	#Builds a 2D array given a file
	arr = []
	fd = open(file, 'r')
	for line in fd:
		arr.append(line.strip().split(','))

	#print('\t'.join(arr[0]))
	return arr
		
	
def print_double_array(arr):
	#Prints a double array all pretty like.
	for element in arr:
		for row in element:
			print('\t'.join(row))
	
def main():
	start = []
	goal = []
	start.append(build_array('testStart1.txt'))
	goal.append(build_array('testGoal1.txt'))
	print 'start config:'
	print_double_array(start)
	print '\ngoal config:'
	print_double_array(goal)
	

#	a = [7, 2, 4]
#	b = [5, 0, 6]
#	c = [8, 3, 1]
#	start = [a, b, c]
#	x = [0, 1, 2]
#	y = [3, 4, 5]
#	z = [6, 7, 8]
#	goal = [x, y, z]
	
#	Print_Double_Array(arr)
    #do stuff here
    
if __name__ == '__main__':
	main()