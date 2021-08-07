import random  #Imports Random Python Library

userChoice = input("What is your move. 'r' for Rock, 'p' for Paper, or 's' for Scissors? ") #Asks the user for their move
userChoice = userChoice.lower() #Convert the user's input to lowercase to easily compare to the computer's choice

print("You chose: " + userChoice) #Prints what the user chose

computerChoice = random.choice(['r', 'p', 's']) #Randomly generate's the computer's choice

print(" The compouter chose: " + computerChoice) #Prints the computer's choice