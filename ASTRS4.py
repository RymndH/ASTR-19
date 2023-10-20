"""
Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical parameters of the animal:
length of the arms (float), length of the legs (float), number of eyes (int), 
does it have a tail? (bool), is it furry? (bool). 
Write an initialization function that sets the values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
"""

def main():

	class Animal:
		#Defines/Initializes the characteristics of the class
		def __init__(self,LOA,LOL,NOE,tail,furry):
			self.LOA = float(LOA)
			self.LOL = float(LOL)
			self.NOE = int(NOE)
			self.tail = bool(tail)
			self.furry = bool(furry)


	#Creates an animal object and declares it's characteristics
	A1 =Animal(8.0, 8.0, 2, True, True)
	#Prints the characteristics of the created animal object
	def PANC(x):
		print(f"The animal's legs are {x.LOL} inches long.")
		print(f"The animal's arms are {x.LOA} inches long.")
		print(f"The animal has {x.NOE} eyes.")
		print(f"The animal has a tail: {x.tail}")
		print(f"The animal is furry: {x.furry}")

	PANC(A1)













if __name__ == "__main__":
	main()

