# 1. Find smallest and biggest elements in an list of n numbers.

numbers = [1, 2, 3, 4, 5, 6, 7]
print(max(numbers), "is the Maximum element in list")
print(min(numbers), "is the Minimum element in list")

# numbers = list(map(int, input("Enter numbers : ").strip().split(" ")))
# maxi = numbers[0]
# mini = numbers[0]

# for i in numbers:
#     if i > maxi:
#         maxi = i

# print(maxi, "is the Maximum element in list")

# for i in numbers:
#     if i < mini:
#         mini = i

# print(mini, "is the Minimum element in list")


# 2. Find the frequency an element in a list of n elements.

numbers = [1, 7, 3, 4, 7, 6, 7, 6, 7]
target = int(input("Enter taget : "))
print("The count of ", target, "in the list :", numbers.count(target))

# numbers = list(map(int, input("Enter numbers : ").strip().split(" ")))
# target = int(input("Enter target : "))

# count = 0
# for i in numbers:
#     if i == target:
#         count += 1

# print("The count of", target, "in the list :", count)

# 3. Remove the duplicates in a list of size n

numbers = list(map(int, input("Enter numbers : ").strip().split(" ")))

is_there = []
for i in numbers:
    if i not in is_there:
        is_there.append(i)

print(is_there)

# **4. Given a number, find very next possible bigger number that has all the digits of the given number.

number = int(input("Enter number : "))
lst_numbers = list(map(int, str(number)))

last_number = lst_numbers[len(str(number))-1]
lst_numbers_reverse = lst_numbers[::-1]
continue_program = False
for i in lst_numbers_reverse:
    if i < last_number:
        mini = i
        continue_program = True
        break

if continue_program:
    for i in range(len(lst_numbers)):
        if lst_numbers[i] == mini:
            mini_idx = i

    mini_sorted = lst_numbers[mini_idx:]
    mini_sorted.sort()
    
    temp = mini_sorted[0]
    mini_sorted[0] = mini_sorted[1]
    mini_sorted[1] = temp
    
    first_lst = lst_numbers[:mini_idx]
    first_lst.extend(mini_sorted)
    result = int("".join(map(str, first_lst)))
    print(result)
else:
    print("Very next possible bigger number is not possible.")

# number = int(input("Enter number : "))
# lst_numbers = list(map(int, str(number)))

# last_number = lst_numbers[len(str(number))-1]
# lst_numbers_reverse = lst_numbers[::-1]
# continue_program = False
# for i in lst_numbers_reverse:
#     if i < last_number:
#         mini = i
#         continue_program = True
#         break

# if continue_program:
#     for i in range(len(lst_numbers)):
#         if lst_numbers[i] == mini:
#             mini_idx = i

#     mini_sorted = lst_numbers[mini_idx:]
#     mini_sorted.sort()
#     smallest_num = mini_sorted[1]
    
#     for i in range(len(lst_numbers)):
#         if lst_numbers[i] == smallest_num:
#             smallest_num_idx = i
    
#     temp = lst_numbers[mini_idx]
#     lst_numbers[mini_idx] = lst_numbers[smallest_num_idx]
#     lst_numbers[smallest_num_idx] = temp
    
#     first_lst = lst_numbers[:mini_idx]
#     second_lst = lst_numbers[mini_idx:]
#     second_lst.sort
#     result = []
#     result.extend(first_lst)
#     result.extend(second_lst)
#     print(result)
# else:
#     print("Very next possible bigger number is not possible.")


# 5. Accpet a number from the user (4 digit number where a digit can repeat at most 2 times )and print the coutn of recursions reqired to arrive at Karpekar's Constant.

def karpekar_constant(num):
    lst_num = list(map(int, str(number)))

    # number = int("".join(map(str, my_list))--------syntax------

    lst_num.sort()
    smallest_num = int("".join(map(str, lst_num)))
    
    lst_num.sort(reverse = True)
    largest_number = int("".join(map(str, lst_num)))

    return largest_number-smallest_num

number = int(input("Enter number : "))
lst_num = list(map(int, str(number)))
ok = True
for i in lst_num:
    if(lst_num.count(i) > 2):
        ok = False

if(len(lst_num) == 4 and ok):
    loop = True
    count = 0
    while loop:
        number = karpekar_constant(number)
        count += 1
        if number == 6174:
            print("Karpekar's Constant and we got at :", count, "time.")
            loop = False
else:
    print("Invaild number")
