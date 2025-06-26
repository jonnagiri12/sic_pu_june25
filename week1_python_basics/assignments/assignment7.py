import math

number = int(input("Enter a postive interger to Check is Perfect square : "))
sqared_number = math.sqrt(number)

for i in range(1, int(sqared_number) + 1):
    if (i*i) == number:
        print(i, "Perfect square of", number)
