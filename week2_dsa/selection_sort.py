def swap(arr, in1, in2):
    temp = arr[in1]
    arr[in1] = arr[in2]
    arr[in2] = temp

array = [6, 3, 7, 2, 77, 23 ,76, 11, 65, 8, 34, 45]

for i in range(len(array)-2):
    min = i
    for j in range(i+1, len(array)-1):
        if array[min] > array[j]:
            min = j
    swap(array, min, i)

print(array)