# This application takes a monthly net cash and bill amount in and divides it into
# weekly amounts and prints those amounts int the console while writing the amounts to a .txt file.

def menu(): # This function when called prints a list of choices the user can input
    print("---***Budget Program***---")
    print("Press 1. Enter Information")
    print("Press 2. Print results")
    print("Press 3. Exit program")
    print("---********Menu********---")
    print("\n")
    
def option1(): # This function collects user input calculates totals and writes contents to a file when called.
    # Variables
    mSalary = ""
    mBills = ""
    wSalary = 0.00
    wBills = 0.00
    netDifference = 0.00
    mDifference = 0.00
    
    validator = False  # Validation to ensure that the input is a number and greater than zero
    while validator == False:
        mSalary = input("Please enter a montly income: ") # Input from user to set the amounts for calculation
        try:
            mSalary = float(mSalary)
        except:
            print("Invalid input. Please enter numbers only")
            continue

        if mSalary <= -1: # Prevents numbers less than zero from being entered
            print("This number cannot be lower than zero")
            continue
        else:
            validator = True

    validator = False  # Validation to ensure that a number is the input and greater than zero
    while  validator == False:
        mBills = input("Please enter total monthly bills: ")  # Input from user to set the amounts for calculation
        try:  
            mBills = float(mBills)
        except:
            print("Invalid input. Please enter numbers only")
            continue
        if mBills <= -1: # Prevents numbers less than zero from being entered
            print("This number cannot be lower than zero")
            continue
        else:
            validator = True

    file = open('Budget.txt', 'w')  #Open/create and name file then write initial user input to the file
    file.write("Monthly income: " +  "\n" + str(mSalary) + '\n')
    file.write("Monthly bills: " +  "\n" +  str(mBills) + '\n')
    file.close()  # Closes the File

    file = open('Budget.txt', 'r')  # Open file to read information for calculation(s)
    income = file.readline()  
    mSalary = file.readline()
    debt = file.readline()
    mBills = file.readline()
    # Calculations
    wSalary = float(mSalary) / 4  # Convert Monthly salary to weekly salary
    wBills = float(mBills) / 4  # Convert monthly bills to weekly bills
    netDifference = wSalary - wBills  #Reduce weekly salary by weekly bills
    mDifference = netDifference * 4  #Total monthly income after bills
    file.close()  # Closes the File
    
    # This section opens the file and appends new amounts and labels to the existing file
    file = open('Budget.txt', 'a')  
    file.write("Weekly pay: " +  '\n' + str(round(wSalary,2)) + '\n')  #Label and write weekly pay to the .txt file
    file.write("Weekly bills: " +  '\n' + str(round(wBills,2)) + '\n')  #Label and write weekly bills to the .txt file
    file.write("Weekly budget: " +  '\n' + str(round(netDifference,2)) + '\n')  #Label and write weekly income after bills to the .txt file
    file.write("Monthly budget: " +  '\n' + str(round(mDifference,2)) + '\n')  #Label and write monthly income after bills to the .txt file
    file.close()  # Closes the File 

def option2(): # This function reads file contents and prints results to the console when called
    file = open('Budget.txt', 'r') 
    fileData = file.read()
    print(fileData)
    file.close()  # Closes the File
    
def option3(): # This function exits the program when called
    exit()

while True:    # loop controls the functions for the menu
    menu()
    option = input("Please enter an option: ") # Input from user

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
    