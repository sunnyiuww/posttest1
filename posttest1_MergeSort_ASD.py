import random
import os
os.system('cls')

def merge_sort (array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array [mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while (i < len(left_arr)):
            array[k] = left_arr[i]
            i += 1
            k += 1
        
        while (j < len(right_arr)):
            array[k] = right_arr[j]
            j += 1
            k += 1

array = []
arr = list(range(1, 30))
array = random.sample(arr, k=10)
merge_sort (array)
print(array)