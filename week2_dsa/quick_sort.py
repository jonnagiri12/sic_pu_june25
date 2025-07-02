def partition (arr, low, high):
    pivot = arr[high]
    k = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        if arr[k] > pivot:
            arr[k], arr[high] = arr[high], arr[k]
    return k
  
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

arr = [1, 7, 2, 98, 34, 12, 65, 87, 23, 55, 73, 9]
quick_sort(arr, 0, len(arr)-1)

print(arr)
