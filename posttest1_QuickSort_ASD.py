import random
import os
os.system('cls')

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]

        left = [x for x in arr[1:] if x <= pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quickSort(left) + [pivot] + quickSort(right)

arr = []
array = list(range(1, 30))
arr = random.sample(array, k=10)
print(f"Sebelum : {arr}")

result = quickSort(arr)
print(f"Sesudah : {result}")

