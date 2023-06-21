# Franklin Means: 6/19/2023
# This program allows the player to guess a randomly assigned number
# and tells them if they are above the number or lower.
import random
lowerLimit = 0
upperLimit = 10

targetNumber = random.randrange(lowerLimit, upperLimit)# This function randomly chosses a number within the stated range
# print(f"The random number is {targetNumber}.\n") # A check to make sure the number is random each time.
guess = ""
while guess != targetNumber:  
    guess = input("Guess The number!\nEnter your guess 0-10: ")# Input from the player
    
    try:# The try except method will prevent letters from being accepted
        guess = int(guess)
    except:
        print("Invalid! Numbers only")
        continue  # Once valid the loop continues to the next step
            
    if guess < 0 or guess > 10: # Prevents numbers less than zero or more than ten from being entered
        print("Enter a number (0-10)")
        continue # Once valid the loop continues to the next step

    elif guess < targetNumber:# This part of the loop shows if your guess is high or low
        print("Sorry the number is Higher")
    elif guess > targetNumber:
        print("Sorry the number is Lower")                     
else:# once the number is correctly guessed the loop ends with a success message
    print("Success!\nThanks for playing!!!")
# End of program