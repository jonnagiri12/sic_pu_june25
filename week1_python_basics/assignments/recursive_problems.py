# 1. Find Factorial of a number

# def fac(number):
#     if number == 1 or number == 0:
#         return 1
#     else:
#         return number * fac(number-1)

# number = int(input("Enter number to find factorial : "))
# print("Factorial of {} is : {}!".format(number, fac(number)))

# 2. Print N Fibo terms with 1 and 2 as 1st 2 terms.

# def fibo(n, number1, number2):
#     if n <= 0:
#         return
#     print(number1, end = " ")
#     number3 = number1 + number2
#     fibo(n-1, number2, number3)

# fibo(5, 1, 2)

# def nth_fibo(number):
#     if number <= 1:
#         return number
#     return nth_fibo(number-1) + nth_fibo(number-2)

# print(nth_fibo(5))

# 5. Accpet a number from the user (4 digit number where a digit can repeat at most 2 times )and print the coutn of recursions reqired to arrive at Karpekar's Constant.

number = int(input("Enter number : "))
str_num = str(number)
lst_num = []
for i in str_num:
    lst_num.append(int(i))
for i in lst_num:
    if(lst_num.count(i) > 2):
        print(number)
