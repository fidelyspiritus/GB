A = int(input())
first, second, current = 1, 1, 2
number = 3
flag = -1
while current <= A:
    if A == current:
        flag = number
    
    first = second
    second = current
    current = second + first
    number += 1
print (flag)