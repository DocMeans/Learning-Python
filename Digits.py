# Franklin Means
# 6/15/2023 Addon to the Loop1 program
# This program randomly selects 2 numbers after user chooses the range (1-9, 10-99, 100-999)
# The user chooses the number of questions they want for the test. 
# The program presents the user with questions and show whether the answer was correct or not.
import random

numberOfTestQuestions = int(input("How many questions? ")) # prompt the user to input how many questions are needed for the test
numberOfDigits = int(input("Number of digits? (1/2/3) ")) # prompt the user to input the number digits they want to add to each number

for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
    if numberOfDigits == 1: # The if and elif statement will randomly select a number within the range the user chose
        number1 = random.randrange(1, 9) # If 1 digit number range is chosen, 
        number2 = random.randrange(1, 9) # The program will randomly select a number from 1 to 9
    elif numberOfDigits == 2:
        number1 = random.randrange(10, 99)  # If 2 digit number range is chosen,
        number2 = random.randrange(10, 99)  # The program will randomly select a number from 10 to 99
    elif numberOfDigits == 3:
        number1 = random.randrange(100, 999)  # If 3 digit number range is chosen,
        number2 = random.randrange(100, 999)  # The program will randomly select a number from 100 to 999

    print("Question " + str(question + 1) + ":") # shows the question number based on the loop iteration 
    
    answer = number1 + number2 # The computation for the outcome

    userAnswer = int(input("What is " + str(number1) + " + " + str(number2) + "? ")) # prompt the user to input the answer
    
    if userAnswer == answer: # the if statement checks to see if the answer is true.
        print("That is correct!\n") # If it is true, the program will print "That is correct!"
    else:
        print("Sorry that is incorrect!\n") # If it is false, the program will print "Sorry that is incorrect!"
        