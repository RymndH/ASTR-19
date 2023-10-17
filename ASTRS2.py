"""Session 2 Prompt: Write a Python that prints the sum of two floating point numbers, 
the difference between two integers, and the product of a floating point number and an 
integer. In each case, have the program print out the data type of the resulting answer.
"""
import numpy as np 
import sys


def main():
	x = 4.3
	y = 5.9
	z = 3
	k = 8

	def sumfunc(x,y):
		summ = x + y
		print(f"The sum of {x} and {y} is {summ}, the datatype is {type(summ)}")


	def diffunc(z,k):
		dif = abs(z+k)
		print(f"The difference of {z} and {k} is {dif}, the datatype is {type(dif)}")


	def prodfunc(k,y):
		prod = (k*y)
		print(f"The product of {k} and {y} is {prod}, the datatype is{type(prod)}")








	sumfunc(x,y)
	diffunc(z,k)
	prodfunc(k,y)







if __name__ == "__main__":
	main()
