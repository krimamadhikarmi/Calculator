import math
print("Select the operation you want to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Square")
print("7. Power")
print("8. Exit")
while(1):
    operation = input("Enter your Choice (1-6):")

    # Addition
    if operation == "1":
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("Sum: " + str(int(num1) + int(num2)))
    # Subtraction
    elif operation == "2":
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("Difference: " + str(int(num1) - int(num2)))
    # Multiplication
    elif operation == "3":
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("Multiply: " + str(int(num1) * int(num2)))
    # Divison
    elif operation == "4":
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("Division:" + str(int(num1) / int(num2)))
    # Square Root
    elif operation == "5":
        num = int(input("Enter the number:"))
        print("Square Root: %f" % (math.sqrt(num)))
    # Square number
    elif operation == "6":
        num = int(input("Enter the number:"))
        print("Square: %d" % (math.pow(num, 2)))
    # Power
    elif operation == "7":
        num = int(input("Enter the number "))
        a = int(input("Enter the power: "))
        print("Power:%d" % (math.pow(num, a)))
    elif operation=="8":
        exit(0)
    else:
        print("Invalid Input")



