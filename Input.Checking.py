'''
Franklin Means  07/02/2023
This program allows the user to select up to ten questions and 1, 2 or 3 digit numbers for this test.
Input validation parameters are no more than 10 questions and the entry has to be a integer greater than zero.
Letters and special characters are not allowed and input will be redirected back to the question.
'''
import random

validator = False  # Validator is used set the exit for the while loop
while validator == False:
    try:
        numberOfTestQuestions = int(input("How many questions? "))
    except ValueError: # Checks if the input is a number and prints the message in it is not.
        print("Invalid input. Please enter numbers only")
        continue
    if numberOfTestQuestions < 1 or numberOfTestQuestions >= 10: # Prevents numbers less than zero or more than ten from being entered
        print("This number cannot be lower than one or higher than ten.")
        continue
    else:
        validator = True # Ends code block Which sets the condition to True

validator = False # resets the validator to False so the next code block can run
while validator == False:
    try:
        numberOfDigits = int(input("Number of digits? (1/2/3) "))
    except ValueError:
        print("Invalid input. Please enter numbers only")
        continue     
    if numberOfDigits < 1 or numberOfDigits > 3:
        print("This number cannot be greater than 3 or less than 1")
        continue
    else:
        validator = True

for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
      
    if numberOfDigits == 1: # Runs the code block if the number is selected
        number1 = random.randrange(1, 10) # Each number is randomly selected
        number2 = random.randrange(1, 10)
    elif numberOfDigits == 2:
        number1 = random.randrange(10, 100)
        number2 = random.randrange(10, 100)
    elif numberOfDigits == 3:
        number1 = random.randrange(100, 1000)
        number2 = random.randrange(100, 1000)
    print(f"Question {str(question + 1)}:") # shows the question number based on the loop iteration 
      
    answer = number1 + number2 # The computation for the questions to check against the user input later.

    validator = False
    while validator == False:
        try:
            userAnswer = int(input(f"What is {str(number1)} + {str(number2)}? ")) # prompt the user to input the answer
        except ValueError:
            print("Invalid input. Please enter numbers only")
            continue
            
        if userAnswer <= -1: 
            print("This number cannot be less than 0")
            continue
        else:
            validator = True
      
    if userAnswer == answer: # the if statement checks to see if the answer is True in which case it prints the message "That is correct!"
        print("That is correct!\n")
    else:
        print("Sorry that is incorrect!\n") 
