import matplotlib.pyplot as plt
import numpy as np

def merge_sort_visual(arr, level=0, pos=None):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_visual(left_half, level + 1, 'left')
        merge_sort_visual(right_half, level + 1, 'right')

        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        visualize_array(arr, level, pos)
    else:
        visualize_array(arr, level, pos)

def visualize_array(arr, level, pos):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(f'Merge Sort Step | Level: {level} | Position: {pos}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_visual(arr)
