import heapq

def find_k_closest_elements(arr, k, x):
    max_heap = []
    
    for num in arr:
        heapq.heappush(max_heap, (-abs(num - x), -num))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    result = [-num for _, num in max_heap]
    result.sort()
    return result


array = [1, 2, 3, 4, 5]
k = 3
x = 3
result = find_k_closest_elements(array, k, x)
print(result)  # Output: [2, 3, 4]
