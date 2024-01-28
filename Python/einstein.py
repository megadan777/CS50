#asking for the mass in grams
mass = float(input("Enter the mass of object(in grams): "))

#Speed of light is known and given in the question
c = 3 * 10 ** 8

#calculating the energy, mass is divided by 1000 to convert it into kilogram
Energy = (mass/1000) * c ** 2 

#printing the output
print(round(Energy, None))