def swap(arr, in1, in2):
    temp = arr[in1]
    arr[in1] = arr[in2]
    arr[in2] = temp

array = [6, 3, 7, 2, 77, 23 ,76, 11, 65, 8, 34, 45]

# Ascending order 
count = 0
sorted = True
for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            swap(array, j, j+1)
            sorted = False
            # count += 1
    if sorted:
        break

print(array)
# print(count)


# descending order
# sorted = True
# for i in range(len(array)-1):
#     for j in range(len(array)-1-i):
#         if array[j] < array[j+1]:
#             swap(array, j, j+1)
#             sorted = False
#     if sorted:
#         break

# print(array)