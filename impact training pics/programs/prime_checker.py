def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


low = int(input())
high = int(input())
for i in range(low, high+1):
    if isPrime(i):
        print(i)
