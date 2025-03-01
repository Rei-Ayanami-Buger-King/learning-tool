#!/usr/bin/python3


def main():
    print("This is a simple addition and subtraction tool to practice cli interaction in python")
    print("\n Would you like to add or subtract?")
    choice = input("Enter choice:")
    if choice == "addition":
        addition()
    else:
        subtraction()

def addition():
    num1 = float(input("What would you like to add?"))
    num2 = float(input("What second number would you like to add?"))
    output = (num1+num2)
    print(output)

    main()




def subtraction():
    num1 = float(input("What would you like to subtract?"))
    num2 = float(input("What second number would you like to subtract?"))
    output = (num1-num2)
    print(output)

    main()



main()