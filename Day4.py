name= input("Enter your name: ")
email= input("Enter your email: ")
mobile= input("Enter your mobile number: ")
print("Please verify your information below:")
print("Name:", name)
print("Email:", email)
print("Mobile:", mobile)
user_input=input("Please select yes to continue / no to exit: (Y/N)")
while user_input=="y" or user_input=="Y":
    print("How can i help you today?")
    print("1. Check your account balance")
    print("2. Transfer money")
    print("3. Deposit money")
    user_choice=input()
def get_team_role(user_choice):
    match user_choice:
        case "1":
            return ""
        case "2":
            return ""
        case "3":
            return ""
        case _:
            return ""

