NumberofShirts = 0
Tshirt = ["small", "medium", "large", "x-large"]
TShirtQty = [0, 0, 0, 0]

# loop to populate the TShirtQty array until the user enters 999
NumberofShirts = int(input("1=small, 2=medium, 3= large, 4=XL, 999 to quit: "))
while NumberofShirts != 999:
    if NumberofShirts > 0 and NumberofShirts < 5:
        Index = NumberofShirts - 1
        TShirtQty[Index] += 1
    else:
        print("Please enter a number between 1 and 4 or 999 to quit")
      
    NumberofShirts = int(input("1=small, 2=medium, 3= large, 4=XL, 999 to quit: "))

Index = 0
while Index < 4:
    print(str(Tshirt[Index]) + " " + str(TShirtQty[Index]))
    Index += 1