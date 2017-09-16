import math
print "Random Number Generator"

#Using the formal Z(i) = (a * Z(i-1) + c) mod m
def uniform_LCG():
	m = float(2 ** 32)
	a = 22695477
	c = 1
	#seed the random number value at 1
	currval = float(1)
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_uniform_LCG.csv", "wb")
	while i < iterations:
		currval = (a * currval + c) % m
		outputFile.write(str(currval/m) + "\n")
		i += 1
	outputFile.close()
	print "10000 random numbers generated and stored in Shah_Devendra_uniform_LCG.csv."

#Using the formula Z(i) = (Z(i-k) + Z(i-j)) mod m 
def uniform_additive():
	m = float(2 ** 32)
	k = 3
	j = 1
	#seed the random number value at 1
	currval = float(1)
	dp = [0 for _ in range(10003)]
	for i in range(10003):
		if i < 3:
			dp[i] = currval
		else:
			dp[i] = (dp[i - j] + dp[i - k]) % m
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_uniform_additive.csv", "wb")
	while i < iterations:
		outputFile.write(str(dp[i+3]/m) + "\n")
		i += 1
	outputFile.close()
	print"10000 random numbers generated and stored in Shah_Devendra_uniform_additive.csv."

#Using the formula Z(i) = (a1*(Z(i-1))**2 + a2*Z(i-1) + c) mod m
def uniform_quadratic():
	a1 = 22695477
	a2 = 134775813
	c = 1
	m = float(2 ** 32)
	#seed the random number value at 1
	currval = float(1)
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_uniform_quadratic.csv", "wb")
	while i < iterations:
		currval = (a1 * (currval ** 2) + a2 * currval + c) % m
		outputFile.write(str(currval/m) + "\n")
		i += 1
	outputFile.close()
	print"10000 random numbers generated and stored in Shah_Devendra_uniform_quadratic.csv."

#function to convert non zero Uniform distribution random numbers to exponential distribution
def uniform_to_exponential(ui, lmbd):
	if ui == 0:
		return 0
	return -1 * (float(1)/lmbd) * math.log(ui)


#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_LCG():
	m = float(2 ** 32)
	a = 22695477
	c = 1
	lmbd = float(1)
	#seed the random number value at 1
	currval = float(1)
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_exponential_LCG.csv", "wb")
	while i < iterations:
		currval = (a * currval + c) % m
		outputFile.write(str(uniform_to_exponential(currval/m, lmbd)) + "\n")
		i += 1
	outputFile.close()
	print "10000 random numbers generated and stored in Shah_Devendra_exponential_LCG.csv."

#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_additive():
	m = float(2 ** 32)
	k = 3
	lmbd = float(1)
	#seed the random number value at 1
	currval = float(1)
	dp = [0 for _ in range(10003)]
	for i in range(10003):
		if i < 3:
			dp[i] = currval
		else:
			dp[i] = (dp[i - 1] + dp[i - k]) % m
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_exponential_additive.csv", "wb")
	while i < iterations:
		outputFile.write(str(uniform_to_exponential(dp[i+3]/m, lmbd)) + "\n")
		i += 1
	outputFile.close()
	print"10000 random numbers generated and stored in Shah_Devendra_exponential_additive.csv."

#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_quadratic():
	a1 = 22695477
	a2 = 134775813
	c = 1
	m = float(2 ** 32)
	lmbd = float(1)
	#seed the random number value at 1
	currval = float(1)
	i = 0
	iterations = 10000
	outputFile = open("Shah_Devendra_exponential_quadratic.csv", "wb")
	while i < iterations:
		currval = (a1 * (currval ** 2) + a2 * currval + c) % m
		outputFile.write(str(uniform_to_exponential(currval/m, lmbd)) + "\n")
		i += 1
	outputFile.close()
	print"10000 random numbers generated and stored in Shah_Devendra_exponential_quadratic.csv."


distribution_choice = input("Which distribution would you like to choose to generate the random numbers?" +
	"Enter 1 for uniform and 2 for exponential distribution. : ")

while (distribution_choice != 1 and distribution_choice != 2):
	print ""
	print "Please enter a valid choice."
	distribution_choice = input("Which distribution would you like to choose to generate the random numbers?" +
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

if distribution_choice == 1 and technique_choice == 1:
	uniform_LCG()
elif distribution_choice == 1 and technique_choice == 2:
	uniform_additive()
elif distribution_choice == 1 and technique_choice == 3:
	uniform_quadratic()
elif distribution_choice == 2 and technique_choice == 1:
	exponential_LCG()
elif distribution_choice == 2 and technique_choice == 2:
	exponential_additive()
elif distribution_choice == 2 and technique_choice == 3:
	exponential_quadratic()