
n = int(input())
a = 65
check = 1
for i in range(n):
    for j in range(i+1):
        if check%2 == 0:
            print(chr(a).lower(),end=" ")
            a += 1
            check += 1
        else:
            print(chr(a).upper(),end=" ")
            a += 1
            check += 1
    print()