# Whats happening? -> creation of simple banking application using python
#Just a simple CLI application banking system in Python i find its more interesting in learning exercise focused on control flow, input handling, and program structure.

name= input("Enter your name: ")
email= input("Enter your email: ")
mobile= input("Enter your mobile number: ")
print("Please verify your information below:")
print("Name:", name)
print("Email:", email)
print("Mobile:", mobile)

def check_balance(balance):
    print(f"Your balance is: {balance}\n\n")

def deposit(balance, amount):
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}\n\n")
    return balance

def transfer(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"Transferred {amount}. New balance: {balance}\n\n")
    else:
        print("Insufficient balance")
        return balance
    return balance

user_input=input("Please select yes to continue / no to exit: (Y/N)")
while user_input=="y" or user_input=="Y":
    print("How can i help you today?")
    print("1. Check your account balance")
    print("2. Transfer money")
    print("3. Deposit money\n\n")
    print("4. Exit")
    user_choice = int(input("Please select an option (1-4): "))
    match user_choice:
        case 1:
            balance = 1000.0  
            check_balance(balance)
        case 2:
            balance = 1000.0  
            amount = float(input("Enter the amount to transfer: "))
            balance = transfer(balance, amount)
        case 3:
            balance = 1000.0  
            amount = float(input("Enter the amount to deposit: "))
            balance = deposit(balance, amount)
        case 4:
            print("Exiting the application. Thank you for using our services.")
        case _:
            print("Invalid choice. Please select a valid option.")

