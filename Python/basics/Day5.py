# Whats happening ? -> creation of simple banking application using python, learning "self" keyword and constructor 

class Atm:
    def __init__(self):       # this is constructor 
          self.pin=""
          self.balance=0

          self.menu()

    def menu(self):
     user_input= input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create a pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
""")
     if user_input=="1":
            self.create_pin()
     elif user_input=="2":
                self.deposit()
     elif user_input=="3":
                self.withdraw()
     elif user_input=="4":
                print("Current balance : ", self.balance)
     elif user_input=="5":
                print("Exit")
     else:
                print("Invalid input")

    def create_pin(self):
        self.pin=input("Enter pin: ")
        print("Pin created successfully")

    def deposit(self):
           temp= input("Enter your pin")
           if temp==self.pin:
                  amount=int(input("Enter the amount to deposit:"))
                  self.balance+=amount
                  print("Deposit successful")
           else:
                    print("Incorrect pin")

    def withdraw(self):
           temp= input("Enter your pin")
           if temp==self.pin:
                  amount=int(input("Enter the amount to withdraw:"))
                  if amount>self.balance:
                        print("Insufficient balance")
                  else:
                         self.balance-=amount
                         print("Withdraw successful")
           else:
            print("Incorrect pin")

from Python.basics.Day5 import Atm
atm=Atm()
atm.deposit()
atm.withdraw()

                  