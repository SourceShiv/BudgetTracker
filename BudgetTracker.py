#Budget Tracker

#OOP approach to create class around object expense
class Expense:
    #constructer to create instances of attributes - amount and category when called
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
    #method to add expense to file in append mode
    def addexpense(self):
        try:
            with open('budget.txt', 'a') as af:
                af.write(f'{self.amount}, {self.category}\n')
                #printing on new line with emoji given in unicode
                print("\n \U00002705 Expense Added Successfully!")
        #catch error as except and print error
        except Exception as e:
            print(f"Error saving expense: {e}")
    #second method is static (no self) to view file which expenses have been written to
    def retrieveexpenses():
        try:
            with open('budget.txt', 'r') as rf:
                rd = rf.read()
                #check if file is empty
                if rd.strip():
                    print("\n \U0001F4CA Expense Summary \n")
                    print(rd)
                else: 
                    print("\n \U0001F4C2 No expenses recorded yet!")
        #send seperate error message if FileNotFoundError arises, and specific error messages for all other errors
        except FileNotFoundError:
            print("File was not found in directory!")
        except Exception as e:
            print(f"Error with file: {e}")
    

#print welcome with moneybag emoji either side in unicode
print("\U0001F4B0 Welcome to Budget Tracker \U0001F4B0")
#will continue loop until break (when exit option 3 is pressed)
while True:
    #input formats numbers in red using ANSI escape codes
    choice = input("""
Choose an option below:

\033[91m1. \033[0mAdd an expense
\033[91m2. \033[0mView summary
\033[91m3. \033[0mExit
                   
Your choice:  """)
    #checks input of choice and runs corresponding method from class Expense
    if choice == '1':
        amount = input("\nEnter the amount: ")
        category = input("Enter the category: ")
        toadd = Expense(amount, category)
        toadd.addexpense()
    elif choice == '2':
        Expense.retrieveexpenses()
    elif choice == '3':
        print("\n Closed Budget Tracker")
        break
    else:
        #returns error for invalid inputs not equal to 1, 2, or 3
        print("Invalid input format, please try again!")


