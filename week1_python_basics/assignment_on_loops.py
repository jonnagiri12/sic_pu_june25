# 1. Find biggest digit in a number

number = int(input("Enter number : "))
str_number = str(number)
max_number = int(str_number[0])

for i in str_number:
    if max_number < int(i):
        max_number = int(i)

print(max_number)

# 2. Find 2nd smallest digit in a number

number = int(input("Enter number : "))
str_number = str(number)
max_number = int(str_number[0])
second_max_number = int(str_number[1])

for i in str_number:
    if max_number < int(i):
        second_max_number = max_number
        max_number = int(i)  
   
print(second_max_number)

# 3. Count number of Prime digits in a number

number = int(input("Enter number : "))
str_number = str(number)
prime_numbers = []

for i in str_number:
    if int(i) > 1:
        count = 0
        for j in range(2, int(i)):
            if int(i) % j == 0:
                count += 1
        if count == 0:
            prime_numbers.append(int(i))
    
print("Count of Prime digits in the number :", len(prime_numbers))

# 4. Print the Prime numbers in decreasing order between m and n (m < n)

print("To Print Prime numbers in decreasing order between m and n (m < n)\nEnter range")
number1 = int(input("Enter number1 :"))
number2 = int(input("Enter number2 :"))

if number1 < number2:
    for i in range(number1, number2+1):
        if i > 1:
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
            if count == 0:
                print(i, end = " ")
else:
    print("Invaild range!")

# 5. Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2

number =  int(input("Enter Nth fibo number : "))
n1 = 1
n2 = 2

if number == 1:
    print(n1)
elif number == 2:
    print(n2)
elif number >= 3:
    for i in range(1, number+1):
        if number == 1:
            print(n1)
        if number == 2:
            print(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        
    print(n2)

# 6. Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)

n = int(input("Enter n value : "))
m = int(input("Enter m value : "))

sum_of_series = 0
if n >= 1 and n <= 4 and m >= 2 and m <= 10:
        for i in range(m):
            numerator = n ** (2*i)
            denominator = 2*i + 1
            sign = (-1)**i
            sum_of_series += (numerator/denominator)*sign
            
print(sum_of_series)
