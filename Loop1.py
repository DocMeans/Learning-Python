# Franklin Means
# 6/14/2023
# This program randomly selects 2 numbers (1-10) and asks the user 
# to give the solution for each question and show whether it was correct or not.
# The program will ask a number of question from given input from the user
import random

numberOfTestQuestions = int(input("How many questions do you want? ")) # prompt the user to input how many questions they want to test

for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
    print("Question " + str(question + 1) + ":") # shows the loop iteration 
    firstNumber = random.randrange(1, 11) # randomly select a number between 1 and 10
    secondNumber = random.randrange(1, 11)
    
    sum = firstNumber + secondNumber # add the two random numbers to get the sum
    
    answer = int(input("What is " + str(firstNumber) + " + " + str(secondNumber) + "? ")) # prompt the user to input their answer
    
    if answer == sum: # the if statement checks to see if the answer is true. 
        print("That is correct!") # If it is true, the program will print "That is correct!"
    else:
        print("Sorry that is incorrect!") # If it is false, the program will print "Sorry that is incorrect!"