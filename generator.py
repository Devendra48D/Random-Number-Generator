import math
print "Random Number Generator"

#Using the formal Z(i) = (a * Z(i-1) + c) mod m
def uniform_LCG(iterations):
	m = float(2 ** 32)
	a = 22695477
	c = 1
	#seed the random number value at 1
	currval = float(1)
	i = 0
	outputFile = open("Shah_Devendra_uniform_LCG.csv", "wb")
	while i < iterations:
		currval = (a * currval + c) % m
		outputFile.write(str(currval/m) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_uniform_LCG.csv."

#Using the formula X(n) = (X(n-24) + X(n-55)) mod m
def uniform_additive(iterations):
	m = float(2 ** 32)
	j = 24
	k = 55
	#seed the random number values
	currvalodd = float(2 ** 30 - 1)
	currvaleven = float(2 ** 30)
	#perform 1500 rough iterations first and then start storing random values
	dp = [0 for _ in range(iterations + k + 1500)]
	for i in range(iterations + k + 1500):
		if i < k:
			if i % 2 == 1:
				dp[i] = currvalodd
			else:
				dp[i] = currvaleven
		else:
			dp[i] = (dp[i - j] + dp[i - k]) % m
	i = 0
	outputFile = open("Shah_Devendra_uniform_additive.csv", "wb")
	while i < iterations + 1500:
		if i >= 1500:
			outputFile.write(str(dp[i+k]/m) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_uniform_additive.csv."

#Using the formula X(n+1) = (d*(X(n) ** 2) + a*X(n) + c) mod m
#tried this does not work, seems to loop over same values 
#in just 5-6 values
#ignore this
def uniform_quadratic_1_faulty(iterations):
	a = 22695477
	d = 134775812
	c = 1
	m = float(2 ** 32)
	#seed the random number value at 1
	currval = float(1)
	i = 0
	outputFile = open("Shah_Devendra_uniform_quadratic.csv", "wb")
	while i < iterations:
		currval = (d * (currval ** 2) + a * currval + c) % m
		outputFile.write(str(currval/m) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + "random numbers generated and stored in Shah_Devendra_uniform_quadratic.csv."

#working version
#used this instead for quadratic 
#X(0)mod 4 = 2 and X(n+1) = X(n)*(X(n) + 1)mod 2e
def uniform_quadratic(iterations):
	m = float(2 ** math.e)
	#seed the random number value at 10
	currval = float(10)
	i = 0
	outputFile = open("Shah_Devendra_uniform_quadratic.csv", "wb")
	while i < iterations:
		currval = (currval * (currval+1)) % m
		outputFile.write(str(currval/m) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_uniform_quadratic.csv."

#function to convert non zero Uniform distribution random numbers to exponential distribution
def uniform_to_exponential(ui, lmbd):
	if ui == 0:
		return 0
	return (-1 * (float(1)/lmbd) * math.log(ui, math.e)) % 1

#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_LCG(iterations):
	m = float(2 ** 32)
	a = 22695477
	c = 1
	arr = []
	#seed the random number value at 1
	currval = float(1)
	i = 0
	outputFile = open("Shah_Devendra_exponential_LCG.csv", "wb")
	while i < iterations:
		currval = (a * currval + c) % m
		arr.append(currval/m)
		i += 1
	i = 0
	lmbd = sum(arr)/float(len(arr))
	while i < iterations:
		outputFile.write(str(uniform_to_exponential(arr[i], lmbd)) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_exponential_LCG.csv."

#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_additive(iterations):
	m = float(2 ** 32)
	j = 24
	k = 55
	#seed the random number values
	currvalodd = float(2 ** 30 - 1)
	currvaleven = float(2 ** 30)
	#perform 1500 rough iterations first and then start storing random values
	dp = [0 for _ in range(iterations + k + 1500)]
	for i in range(iterations + k + 1500):
		if i < k:
			if i % 2 == 1:
				dp[i] = currvalodd
			else:
				dp[i] = currvaleven
		else:
			dp[i] = (dp[i - j] + dp[i - k]) % m
	i = 0
	outputFile = open("Shah_Devendra_exponential_additive.csv", "wb")
	arr = []
	while i < iterations + 1500:
		if i >= 1500:
			arr.append(dp[i+k]/m)
		i += 1
	lmbd = sum(arr)/float(len(arr))
	i = 0
	while i < iterations:
		outputFile.write(str(uniform_to_exponential(arr[i], lmbd)) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_exponential_additive.csv."

#use uniform_to_exponential function to convert uniform distribution to exponential distribution
def exponential_quadratic(iterations):
	m = float(2 ** math.e)
	#seed the random number value at 10
	currval = float(10)
	i = 0
	arr = []
	outputFile = open("Shah_Devendra_exponential_quadratic.csv", "wb")
	while i < iterations:
		currval = (currval * (currval+1)) % m
		arr.append(currval/m)
		i += 1
	lmbd = sum(arr)/float(len(arr))
	i = 0
	while i < iterations:
		outputFile.write(str(uniform_to_exponential(arr[i], lmbd)) + ",\n")
		i += 1
	outputFile.close()
	print str(iterations) + " random numbers generated and stored in Shah_Devendra_exponential_quadratic.csv."


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

iteration_count = input("Please enter the number of random numbers you would like to generate." +
	"Please enter a valid positive number. : ")
while  iteration_count < 1 or isinstance(iteration_count, int) != True:
	print ""
	print "Please enter a valid number"
	iteration_count = input("Please enter the number of random numbers you would like to generate." +
	"Please enter a valid positive number. : ")
	print ""



print "distribution_choice: " + str(distribution_choice) + " technique_choice: " + str(technique_choice)
print "Number of random numbers to generate: " + str(iteration_count)


if distribution_choice == 1 and technique_choice == 1:
	uniform_LCG(iteration_count)
elif distribution_choice == 1 and technique_choice == 2:
	uniform_additive(iteration_count)
elif distribution_choice == 1 and technique_choice == 3:
	uniform_quadratic(iteration_count)
elif distribution_choice == 2 and technique_choice == 1:
	exponential_LCG(iteration_count)
elif distribution_choice == 2 and technique_choice == 2:
	exponential_additive(iteration_count)
elif distribution_choice == 2 and technique_choice == 3:
	exponential_quadratic(iteration_count)