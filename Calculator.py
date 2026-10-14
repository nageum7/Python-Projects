#Project 1
#Calculator
while True:
    try:
        #This is the list of inputs the user will see in terminal
        inputOne = float(input("Enter the First Number: "))
        inputTwo = float(input("Enter the Second Number: "))
        arith = input("Enter the arithmetic operation(+,-,*,/): ")

        if arith == "+":
            print(inputOne + inputTwo)
        elif arith == "-":
            print(inputOne - inputTwo)
        elif arith == "*":
            print(inputOne * inputTwo)
        elif arith == "/":
            print(inputOne / inputTwo)
        else:
            print("Please enter a valid artarithmetic")

    except ValueError:
        print("Please enter a valid input!")