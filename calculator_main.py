from calcPackage.calculator_functions import *
while(True):

    print("\n********Calculator Menu*********")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Quit")
    print("***********************************")

    choice = int(input("Enter your choice :"))
    if (choice > 5):
        print("Re-Enter choice")
        continue
    elif(choice == 5):
        break

    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number  2: "))


    if (choice == 1):
        print("\tResult: ", addition(num1, num2))
    elif (choice == 2):
        print("\tResult: ", subtraction(num1, num2))
    elif (choice == 3):
        print("\tResult: ", multiplication(num1, num2))
    else:
        print("\tResult: ", division(num1, num2))
