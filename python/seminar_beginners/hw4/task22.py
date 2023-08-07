#from random import randint
#n, m = 24, 35
#first_list = [randint(0, 79) for _ in range(n)]
#second_list = [randint(0, 145) for _ in range(m)]

n, m = [int(i) for i in input().split()]
first_list = [int(input()) for _ in range(n)]
second_list = [int(input()) for _ in range(m)]
result = []

for number in set (first_list):
    if number in second_list:
        result.append(number)
result.reverse

print(result)