# This application takes a monthly net cash and bill amount in and divides it into
# weekly amounts and prints those amounts int the console while writing the amounts to a .txt file.

def menu(): # This function when called prints a list of choices the user can input
    print("------Budget Program------\nPress 1. Enter Information\nPress 2. Print results")
    print("Press 3. Exit program\n-----------Menu-----------\n")
    
def option1(): # This function collects user input calculates totals and writes contents to a file when called.
    mSalary = "" # Variables
    mBills = ""
    wSalary = 0.00
    wBills = 0.00
    netDifference = 0.00
    mDifference = 0.00
    mSalary = input("Please enter a montly income: ") # Get the inputs from the user
    mBills = input("Please enter total monthly bills: ")
    validator(mSalary, mBills) # Validates the inputs
    mSalary = float(mSalary) # Convert the inputs to a floating point number
    mBills = float(mBills)
    file = open('Budget.txt', 'w')  #Open/create and name file then write initial user input to the file
    file.write(f"Monthly income: \n {mSalary} \n")
    file.write(f"Monthly bills: \n {mBills} \n")
    file.close()  # Closes the File

    # Calculations
    wSalary = float(mSalary) / 4  # Convert Monthly salary to weekly salary
    wBills = float(mBills) / 4  # Convert monthly bills to weekly bills
    netDifference = wSalary - wBills  #Reduce weekly salary by weekly bills
    mDifference = netDifference * 4  #Total monthly income after bills
    file.close()  # Closes the File
    
    # This section opens the file and appends new amounts and labels to the existing file
    file = open('Budget.txt', 'a')  
    file.write(f"Weekly pay: \n {round(wSalary,2)} \n")  #Label and write outputs to the .txt file
    file.write(f"Weekly bills: \n {round(wBills,2)} \n")  
    file.write(f"Weekly budget: \n {round(netDifference,2)} \n")  
    file.write(f"Monthly budget: \n {round(mDifference,2)} \n")  
    file.close()  # Closes the File 

def validator(mSalary, mBills):
    validator = False  # Validation to ensure that the input is a number and greater than zero
    while validator == False:
        try:
            mSalary = float(mSalary)
            mBills = float(mBills)
        except:
            print("Invalid input. Please enter numbers only")
            continue

        if mSalary <= -1 or mBills <= -1: # Prevents numbers less than zero from being entered
            print("This number cannot be lower than zero")
            continue
        else:
            validator = True
    return mSalary, mBills

def option2(): # This function reads file contents and prints results to the console when called
    print("-----Result--------")
    file = open('Budget.txt', 'r') 
    fileData = file.read()
    print(fileData)
    file.close()  # Closes the File
    
def option3(): # This function exits the program when called
    exit()

while True:    # loop controls the functions for the menu
    menu()
    option = input("Please enter an option: ") # Input from user to choose an option
    print()
    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    else:
        print("Invalid input, Please try again") 
        print("\n")
    input("Press enter to return to menu")
    print("\n")
    