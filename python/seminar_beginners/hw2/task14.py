#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input())
number = 1

while number < n:
    print(number, end = ",")
    number *= 2 
