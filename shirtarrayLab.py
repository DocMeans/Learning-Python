Tshirt = ["small", "medium", "large", "x-large"]
TShirtQty = [0, 0, 0, 0]

# loop to populate the TShirtQty array until the user enters 999
NumberOfShirts = int(input("1=small, 2=medium, 3= large, 4=XL, 999 to quit: "))
while NumberOfShirts != 999:
    if 0 < NumberOfShirts < 5:
        Index = NumberOfShirts - 1
        TShirtQty[Index] += 1
    else:
        print("Please enter a number between 1 and 4 or 999 to quit")
      
    NumberOfShirts = int(input("1=small, 2=medium, 3= large, 4=XL, 999 to quit: "))

Index = 0
while Index < 4:
    print(str(Tshirt[Index]) + " " + str(TShirtQty[Index]))
    Index += 1
print("Thank You for your business!")
