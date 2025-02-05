def checkPerfectNumber(num):
        stack = []
        res =  0
        for i in range(1,(num//2)+1):
            if num % i == 0:
                stack.append(i)
        print(stack)
        for element in stack:
            res += element
        print(res)
        if res == num:
            return True
        else:
            return False
print(checkPerfectNumber(28))