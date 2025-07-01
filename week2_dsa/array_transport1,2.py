# Array transport -> 1 

n_fitst = int(input("Enter first list count : "))
first_lst = list(map(int, input("Enter numbers :").strip().split()))
n_second = int(input("Enter second list count : "))
second_lst = list(map(int, input("Enter numbers :").strip().split()))

missing = []
for i in second_lst:
    if i not in first_lst:
        missing.append(i)
    else:
        first_lst.remove(i)
    
missing.sort()
print(missing)

# Array transport -> 2

# n_fitst = int(input("Enter first list count : "))
# first_lst = list(map(int, input("Enter numbers :").strip().split()))
# n_second = int(input("Enter second list count : "))
# second_lst = list(map(int, input("Enter numbers :").strip().split()))

# for i in second_lst:
#     if i in first_lst:
#         first_lst.remove(i)
#     else:
#         print(i, end = " ")
