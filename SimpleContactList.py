# Franklin Means CIT-244 9/7/2023
# This program allows the user to view current contact information and add new contacts
# by last name, first name and email
'''Project one'''
class Contact(object):
    '''Class for contacts'''
    contacts = []
    def __init__(self, first_name, last_name, email):
        self.fname = first_name
        self.lname = last_name
        self.mail = email

    def show_contacts(contacts):
        '''this function shows contacts in the console when called'''

        print("----------Contacts------------") # for asthetics
        print("Last Name\tFirst Name\t\tEmail")
        for contact in contacts: # this loop reads the list item by item
            print(f"{contact.lname}\t\t{contact.fname}\t\t\t{contact.mail}")
        print("------------------------------") # for asthetics

# ----------------------End Class--------------------

def add_contact(contacts):
    '''Adds contacts'''

    print("Enter contacts information")
    print("--------------------------") # for asthetics
    fname = input("Enter contacts first name: ") # user input
    lname = input("Enter contacts last name: ")
    mail = input("Enter email: ")
    print()
    new_contact = Contact(fname, lname, mail)
    contacts.append(new_contact)

def menu(contacts):
    '''this runs the main program which shows a menu and calls the appropriate functions'''

    while True:
        # The menu printed to screen
        print("----------Menu----------------")
        print("1. Display contacts\n2. Create contact\n3. Exit program")
        print("----------Option--------------")
        option = input("Select an option. (1, 2, 3): ")
        #When an option is chosen, that function will be called
        if option == "1":
            Contact.show_contacts(contacts)

        elif option == "2":
            add_contact(contacts)

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid input, Please enter a number 1, 2 or 3")

def main():
    '''Run the program'''
    menu(Contact.contacts)

if __name__ == "__main__":
    main()
