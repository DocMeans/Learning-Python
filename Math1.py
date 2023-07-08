import random
from operator import sub, add, mul

'''
 Franklin Means
 6/14/2023 - 07/02/2023
 In the menu the user can choose between addition, subtraction, multiplication or a random question.
 In the random section each question has a random operator as well as random numbers.
 The scores are on a percentage scale with appropriate letter grades
 which is output and the end of the test.
'''
numberOfTestQuestions = int(input("How many questions do you want? ")) # prompt the user to input the numbers of questions they want.
print("Which operator \n1. addition \n2. subtraction")# The menu
print("3. multiplication \n4. Surprise Me!") 
operator = int(input("Choice: ")) # user chooses operator
print()
score = 0

for question in range(numberOfTestQuestions): # This loop will run for each question the user requested
    
    if operator == 1 or operator == 2 or operator == 3:
        print(f"Question {question + 1}:") # shows the loop iteration 
        firstNumber = random.randrange(1, 11) # randomly select a number between 1 and 10
        secondNumber = random.randrange(1, 11)
        match operator: # Selects the correct case to match the operator the user chose
            case 1:
                operation = firstNumber + secondNumber
                answer = int(input(f"What is {firstNumber} + {secondNumber}? "))
            case 2:
                operation = firstNumber - secondNumber
                answer = int(input(f"What is {firstNumber} - {secondNumber}? "))
            case 3:
                operation = firstNumber * secondNumber
                answer = int(input(f"What is {firstNumber} * {secondNumber}? "))
        if answer == operation: 
            print()
            score += 1
        else:
            print()
    else: # This part runs if anything other than the first three options were not taken. This is the Surprise
        print("done")
        firstNumber = random.randrange(1, 11)
        secondNumber = random.randrange(1, 11)
        operators = {"+": add, "-": sub, "*": mul} # Dictionary of operators
        keys = list(operators) 
        operator = random.choice(keys) # the use of key:value pairs to choose random operators.
        print(f"Question {question + 1}:")
        answer = int(input(f"What is {firstNumber} {operator} {secondNumber}? ")) #  shows the question and requests an answer
        if answer == (operators[operator](firstNumber, secondNumber)): # Check to see if the operator and answer match. 
            print()
            score += 1
        else:
            print() 

outcome = int(score / numberOfTestQuestions * 100) # Grading and listed number of correct answers
print("------------Score-----------")
if outcome > 90:
    print(f"Got got {score} out of {numberOfTestQuestions} Correct!")
    print(f"Score: {outcome}% = A")
    print()
elif outcome >= 80 and outcome < 90:
    print(f"Got got {score} out of {numberOfTestQuestions} Correct!")
    print(f"Score: {outcome}% = B")  
    print()
elif outcome >= 70 and outcome < 80:
    print(f"Got got {score} out of {numberOfTestQuestions} Correct!")
    print(f"Score: {outcome}% = C")
    print()
elif outcome >= 60 and outcome < 70:
    print(f"Got got {score} out of {numberOfTestQuestions} Correct!")
    print(f"Score: {outcome}% = D")
    print()
else:
    print(f"Got got {score} out of {numberOfTestQuestions} Correct!")
    print(f"Score: {outcome}% = F")
    print()
