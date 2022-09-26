# This is a calculator that will take the user's inputs and give the standard deviation and mean of the set of values.

# The user is asked to input the quantity of the data set and ensure that the value is not '0'.
while True:
	try:	
		n = int(input("Enter the quantity of values being analysed: "))
		if n == 0:
			print("You need at least two values in your data set.")		
		else:
			break
	except:
		ValueError
		

Werte_der_Analyse = []
Nominator_der_Formule = 0

# The user is asked if he/she is sure of the quantity inputted in the data set.
sicherheitshalber_nachfragen1 = input(f"Are you certain that 'n = {n}' is the data quantity you wish to analyse. Enter 'YES' if correct: ")
while True:
	if sicherheitshalber_nachfragen1.upper() == 'YES' or sicherheitshalber_nachfragen1.upper() == 'Y':
		for i in range(n):
			# Values are added to the empty list using the 'list.append' function and a for-loop, when the user confirms that the data quantity inputted is correct.
			Werte_der_Analyse.append(float(input("Enter your value: ")))
		print(Werte_der_Analyse)

		
		while True:
			sicherheitshalber_nachfragen2 = input(f"Are you certain that {Werte_der_Analyse} corresponds with the data set that you wish to work with. Enter 'YES' if correct: ")
			if sicherheitshalber_nachfragen2.upper() == 'YES' or sicherheitshalber_nachfragen2.upper() == 'Y':
				avg_Werte_der_Analyse = sum(Werte_der_Analyse) / n
				break
				
			else:
				# The user is enabled to make corrections without starting over the program.
				Korrektionenummer = int(input("Enter the number of corrections you think you will need to make to the displayed data set: "))

				for i in range (0,Korrektionenummer): 
					print("Enter the column number, 'col_num', of the value you wish to change. For example, to change the value of the first column, enter '0' as the column number.")
					col_num = int(input("col_num = " ))
					while True:
						try:
							Werte_der_Analyse[col_num] = float(input(f"Enter new value for column {col_num + 1}: "))
							print(Werte_der_Analyse)
							break
						except:
							IndexError
							print(Werte_der_Analyse)
						break
					if i == Korrektionenummer - 1:
						while True:
							try:
								Korrektionenummer += int(input("Do you need any more corrections? Enter the number of additional corrections needed: "))
								break
							except:
								ValueError
						sicherheitshalber_nachfragen4 = int(input("Do you want to work with a bigger data set quantity? Enter the additional quantity: "))
						while True:
							try:
								for u in range (0,sicherheitshalber_nachfragen4):
									Werte_der_Analyse.append(float(input("Enter your value: ")))
									print(Werte_der_Analyse)
								break
							except:
								ValueError
						sicherheitshalber_nachfragen5 = int(input("Do you want to work with a smaller data set quantity? Enter the quantity to be reduced: "))
						while True:
							try:
								for y in range (0,sicherheitshalber_nachfragen5):
									Werte_der_Analyse[y] = 0.0
									print(Werte_der_Analyse)
								break
							except:
								ValueError
		
		
		for i in range(0,n):
			Nominator_der_Formule += (Werte_der_Analyse[i] - avg_Werte_der_Analyse)**2

		# The user is asked to select whether the data set is a sample of a population or the total population. Only two responses are accepted: 'P'- Population or 'S'- Sample.	
		while True:
			p1gerne = input("Enter 'P' for population or 'S' for sample: ")
			
			if p1gerne.upper() == 'P':
				Standardabweichung_Werte_der_Analyse = pow(Nominator_der_Formule / (n), 0.5)
				break
			elif p1gerne.upper() == 'S':
				Standardabweichung_Werte_der_Analyse = pow(Nominator_der_Formule / (n - 1), 0.5)
				break
			elif p1gerne.upper() != 'P' or p1gerne.upper() != 'S':
				print("Please enter either 'P' or 'S'.")
		break	            
	else:
		# If the data set quantity does not correspond with what the user intended to input, the user is given another chance to input the correct quantity and is then asked again if the new quantity is the desired.
		n = int(input("Enter the quantity of values being analysed: "))	
		sicherheitshalber_nachfragen1 = input(f"Are you certain that 'n = {n}' is the data quantity you wish to analyse. Enter 'YES' if correct: ")       

# The standard deviation and mean of the data set are printed.					
print(f"""
	The standard deviation of the data set is: {Standardabweichung_Werte_der_Analyse}
	The mean of the data set is: {avg_Werte_der_Analyse}
	""")


