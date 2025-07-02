# binary serach (Iterately)🦖🦖🦖🦖🦖

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter search element in the range of 10 : "))
low = 0
high = len(array)-1

while low <= high:
    mid = (high + low)//2
    if array[mid] == target:
        print("Target found")
        break
    elif array[mid] > target:
        high = mid - 1
    elif array[mid] < target:
        low = mid + 1


# Binary search (Recursion)🦖🦖🦖🦖🦖

def binary_search (arr, low, high, target):
    mid = low + (high-low)//2
    if arr[mid] == target:
        return print("Target found")
    elif arr[mid] > target:
        binary_search(arr, low, mid-1, target)
    else:
        binary_search(arr, mid+1, high, target)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter search element in the range of 10 : "))

binary_search(array, 0, len(array)-1, target)