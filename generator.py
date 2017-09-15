print "Random Number Generator"

def uniform_LCG():
	pass


def uniform_additive():
	pass

def uniform_quadratic():
	pass


def exponential_LCG():
	pass


def exponential_additive():
	pass

def exponential_quadratic():
	pass

distribution_choice = input("Which distribution would you like to choose to generate the random numbers?" +
	"Enter 1 for uniform and 2 for exponential distribution. : ")

while (distribution_choice != 1 and distribution_choice != 2):
	print ""
	print "Please enter a valid choice."
	distribution_choice = input("Which distribution would you like to choose to generate the random numbers?" 
		" Enter 1 for uniform and 2 for exponential distribution. : ")

print ""
technique_choice = input("What technique would you like to choose to generate the random numbers?" +
	"Enter 1 for LCG, 2 for additive, and 3 for quadratic technique. : ")
while (technique_choice != 1 and technique_choice != 2 and technique_choice != 3):
	print ""
	print "Please enter a valid choice."
	technique_choice = input("What technique would you like to choose to generate the random numbers?" + 
	 "Enter 1 for LCG, 2 for additive, and 3 for quadratic technique. : ")


print "distribution_choice: " + str(distribution_choice) + " technique_choice: " + str(technique_choice)
