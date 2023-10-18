"""
Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, including a main program function.
"""
import numpy as np
import sys


def main():

	table = {}
	
	#Loops through values 0 to 2 1000 times and adds the key value pairs of x and sin(x) to a larger dictionary
	def tablegen():
		x = 0.0
		for i in range(1001):
			table.update({round(x,4):round(np.sin(x),4)})
			x += 0.002
		print(table)


	

	


	tablegen()













if __name__ == "__main__":
	main()