'''
Developer: Ghaizar A. Bautista
Title: BubbleSort
'''

import os
os.system('cls')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f"Step {i+1}: {arr}")
        if not swapped:
            break


letters = ['d', 's', 'm', 'r', 'a', 'e']
print("Unsorted array:", letters)
print("\nSorting process:")
bubble_sort(letters)
print("\nSorted array:", letters)