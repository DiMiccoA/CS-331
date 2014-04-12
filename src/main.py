'''
Created on Apr 12, 2014

@author: anton_000
'''
def Print_Double_Array(arr):
	#Prints a double array all pretty like.
	for row in arr:
		print('\t'.join(map(str, row)))
	
def main():
	a = [7, 2, 4]
	b = [5, 0, 6]
	c = [8, 3, 1]
	start = [a, b, c]
	x = [0, 1, 2]
	y = [3, 4, 5]
	z = [6, 7, 8]
	goal = [x, y, z]
	
	Print_Double_Array(arr)
    #do stuff here
    
if __name__ == '__main__':
	main()