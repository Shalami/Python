#-------------------------------------------------------------------------------
# Name:        passGen
# Purpose:     Your standard password generator.
#
# Author:      Noah Myers
#
# Created:     05/12/2014
# Copyright:   (c) Noah Myers 2014
#-------------------------------------------------------------------------------
import string
import random
import time

def main():
    try:
        userLength = int(input("How long would you like your password? - ")) #Ask the user for a length.
        #If their chosen length is less than six, print a suggestive message.
        if userLength < 6:
            print("The strength of your password length is questionable.\n")
        numberPass = int(input("How many passwords would you like? - ")) #Ask for how many passwords to create.
        for i in range(numberPass): #Loop the write function for the amount of times specified by the user.
            write(passGen(userLength))#Call the write function with the parameter being the returned value from the passGen function.
        print(str(numberPass), "passwords written to 'passw.txt'\nIt is recommended that you do not keep passwords in this file.\n") #Print a success message.
        time.sleep(3) #Pause the program for 3 seconds.
    except ValueError:
        print("Error: please enter an integer.\n")
        main()

def passGen(length):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits #Assign every letter of the alphabet and digits 0-9 to 'chars'.
    chars = ''.join(i for i in chars if i not in "LlIi0Oo") #Remove characters that could cause confusion.
    passw = "" #Create an empty variable 'passw', stores the password.
    for i in range(length): #Loop for the range of the length variable. User specified.
        passw += str(random.choice(chars)) #Append a random character from 'chars' to 'passw'.
    passw += str(" created at " + time.strftime("%H:%M") + "\n")
    return(passw) #Return the complete password.

def write(text):
    op = open("passw.txt", "a") #Open the file 'passw.txt', or create it.
    op.write(text) #Append the variable 'text' to the files.
    op.close() #Close the file.

if __name__ == '__main__':
    main()