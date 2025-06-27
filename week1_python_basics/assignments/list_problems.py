# 1. Find smallest and biggest elements in an list of n numbers.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(max(numbers), "is the Maximum element in list")
# print(min(numbers), "is the Minimum element in list")

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

# numbers = [1, 7, 3, 4, 7, 6, 7, 6, 7]
# print("The count of 7 in the list :", numbers.count(7))

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