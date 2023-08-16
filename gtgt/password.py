#1 set the password.
password = "python"

#2 make a guess variable to store your password.
guess = ""

#3 make a while loop so that the user can try again if the user puts a wrong password.
while password != guess:

#4 this will ask the user for the password.
    guess = input("Enter password: ")
    
    if password == guess:
        print("login success.")
    else:
        print("Incorrect password, try again.")
    