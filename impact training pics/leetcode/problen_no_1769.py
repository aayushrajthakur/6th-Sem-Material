def minoperation(boxes):
    n = len(boxes)
    res = []
    for i in range(n):
        count = 0
        for j in range(n):
            if boxes[j] == "1":
                count += abs(i-j)
        res.append(count)
    return res
boxes = "001011"
result = minoperation(boxes)
print(result)