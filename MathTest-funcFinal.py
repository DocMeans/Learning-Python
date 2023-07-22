import random
from operator import sub, add, mul # This is for the random function as I used a dictionary to make the function work

def addition(): # option 1
    score = 0
    numberOfTestQuestions = int(input("How many questions do you want? "))  # prompt the user to input how many questions they want to test
    numberOfDigits = int(input("Number of digits? (1/2/3) "))
    for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
      if numberOfDigits == 1: # The if and elif statement will randomly select a number within the range the user chose
          firstNumber = random.randrange(1, 10) # If 1 digit number range is chosen, 
          secondNumber = random.randrange(1, 10) # The program will randomly select a number from 1 to 9
      elif numberOfDigits == 2:
          firstNumber = random.randrange(10, 100)  # If 2 digit number range is chosen,
          secondNumber = random.randrange(10, 100)  # The program will randomly select a number from 10 to 99
      elif numberOfDigits == 3:
          firstNumber = random.randrange(100, 1000)  # If 3 digit number range is chosen,
          secondNumber = random.randrange(100, 1000)  # The program will randomly select a number from 100 to 999
      print(f"Question {question + 1}:") # Numbers the question sequentially
      add = firstNumber + secondNumber
      answer = int(input(f"What is {firstNumber} + {secondNumber}? "))
      if answer == add:
          score += 1
      else:
          pass
    outcome(score, numberOfTestQuestions)

def subtract(): # option 2
    score = 0
    numberOfTestQuestions = int(input("How many questions do you want? "))  # prompt the user to input how many questions they want to test
    numberOfDigits = int(input("Number of digits? (1/2/3) "))
    for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
      if numberOfDigits == 1: # The if and elif statement will randomly select a number within the range the user chose
          firstNumber = random.randrange(1, 10) # If 1 digit number range is chosen, 
          secondNumber = random.randrange(1, 10) # The program will randomly select a number from 1 to 9
      elif numberOfDigits == 2:
          firstNumber = random.randrange(10, 100)  # If 2 digit number range is chosen,
          secondNumber = random.randrange(10, 100)  # The program will randomly select a number from 10 to 99
      elif numberOfDigits == 3:
          firstNumber = random.randrange(100, 1000)  # If 3 digit number range is chosen,
          secondNumber = random.randrange(100, 1000)  # The program will randomly select a number from 100 to 999
      print(f"Question {question + 1}:")
      sub = firstNumber - secondNumber
      answer = int(input(f"What is {firstNumber} - {secondNumber}? "))
      if answer == sub:
          score += 1
      else:
          pass
    outcome(score, numberOfTestQuestions)

def multiply(): # option 3
    score = 0
    numberOfTestQuestions = int(input("How many questions do you want? "))  # prompt the user to input how many questions they want to test
    numberOfDigits = int(input("Number of digits? (1/2/3) "))
    for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
      if numberOfDigits == 1: # The if and elif statement will randomly select a number within the range the user chose
          firstNumber = random.randrange(1, 10) # If 1 digit number range is chosen, 
          secondNumber = random.randrange(1, 10) # The program will randomly select a number from 1 to 9
      elif numberOfDigits == 2:
          firstNumber = random.randrange(10, 100)  # If 2 digit number range is chosen,
          secondNumber = random.randrange(10, 100)  # The program will randomly select a number from 10 to 99
      elif numberOfDigits == 3:
          firstNumber = random.randrange(100, 1000)  # If 3 digit number range is chosen,
          secondNumber = random.randrange(100, 1000)  # The program will randomly select a number from 100 to 999
      print(f"Question {question + 1}:")
      sub = firstNumber - secondNumber
      answer = int(input(f"What is {firstNumber} * {secondNumber}? "))
      if answer == sub:
          score += 1
      else:
          pass
    outcome(score, numberOfTestQuestions)

def randomChoice(): # option 4 
    score = 0
    numberOfTestQuestions = int(input("How many questions do you want? ")) # prompt the user to input how many questions they want to test
    numberOfDigits = int(input("Number of digits? (1/2/3) "))
    for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
      if numberOfDigits == 1: # The if and elif statement will randomly select a number within the range the user chose
          firstNumber = random.randrange(1, 10) # If 1 digit number range is chosen, 
          secondNumber = random.randrange(1, 10) # The program will randomly select a number from 1 to 9
      elif numberOfDigits == 2:
          firstNumber = random.randrange(10, 100)  # If 2 digit number range is chosen,
          secondNumber = random.randrange(10, 100)  # The program will randomly select a number from 10 to 99
      elif numberOfDigits == 3:
          firstNumber = random.randrange(100, 1000)  # If 3 digit number range is chosen,
          secondNumber = random.randrange(100, 1000)  # The program will randomly select a number from 100 to 999
      print(f"Question {question + 1}:")      
      operators = {"+": add, "-": sub, "*": mul}
      keys = list(operators)     
      operator = random.choice(keys)
      (f"Question {question + 1}:")
      answer = int(input(f"What is {firstNumber} {operator} {secondNumber}? ")) 
      if answer == (operators[operator](firstNumber, secondNumber)): 
          score += 1
      else: 
          pass
    outcome(score, numberOfTestQuestions)

def outcome(score, numberOfTestQuestions):
    outcome = int(score / numberOfTestQuestions * 100)
    print("------------Score-----------")
    if outcome >= 90:
        print(f"Score: {outcome}% = A")
    elif outcome >= 80 and outcome < 90:
        print(f"Score: {outcome}% = B")
    elif outcome >= 70 and outcome < 80:
        print(f"Score: {outcome}% = C")
    elif outcome >= 60 and outcome < 70:
        print(f"Score: {outcome}% = D")
    else:
        print(f"Score: {outcome}% = F")

def menu(): # This function when called prints a list of choices the user can input
    print()
    print("-----------Menu-------------\nPress 1. for addition\nPress 2. for subtraction")
    print("Press 3. for multiplication\nPress 4. Surprise me!\nPress 9. to quit\n----------------------------")
    print()

while True:    # loop controls the functions for the menu
    menu()
    option = input("Please enter an option: ") # Input from user
    if option == "1":
        addition()
    elif option == "2":
        subtract()
    elif option == "3":
        multiply()
    elif option == "4":
        randomChoice()
    elif option == "9":
        quit()
    else:
        print("Invalid input, Please try again")
        print("\n")
    input("Press enter to return to menu")