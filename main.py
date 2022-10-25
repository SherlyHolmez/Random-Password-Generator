import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be?\n"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)
    print("")
    print("Your generated password is:\n" + password)
    print("")
    print('---------------------------------------------------------')
while True:
    option = input("Do you want to generate a new password? (Y/N)\n")

    if option == "Y" or option == "y":
        generate_password()
    elif option == "N" or option == "n":
        print("Thanks for using the password generator!")
        exit()
    else:
        print('')
        print("Invalid input")
        print('')
