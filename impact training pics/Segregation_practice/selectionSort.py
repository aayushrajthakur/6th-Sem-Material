def selectionSort(array):
    m = len(array)
    for i in range(m):
        minIdx = i
        for j in range(i+1,m):
            if array[j] < array[minIdx]:
                minIdx = j
        array[minIdx], array[i] = array[i], array[minIdx]
    return array

array = [4,1,6,8,34,9]
print(selectionSort(array))