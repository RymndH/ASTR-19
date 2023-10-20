"""Write a Python program that defines a function f(x) that returns x**3 + 8. 
In the main function of the program, call f(x) with x = 9 and print the result.  
Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
"""

def main():

	#Function that returns a number to the power of 3 plus 8, if the returned value is larger than 27 it returns "YAY!
	def tfunc(x):

		ans = ((x**3)+8)
		if ans > 27:
			ans = "YAY!"

		return ans




	print(tfunc(9))


if __name__ == "__main__":
	main()

