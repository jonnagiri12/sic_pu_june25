number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number : "))

if number1 < number2:
    if number1 < number3:
        print(number1, "is smallest number.")
    else:
        print(number3, "is samllest number.")
else:
    if number2 < number3:
        print(number2, "is smallest number.")
    else:
        print(number3, "is smallest number")
