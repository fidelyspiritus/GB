#Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

from random import uniform
number = uniform(0,1258)
main = int(number) 
tail = number - main
sum = 0
print(f"Число {number}, целая часть = {main}, дробная часть = {tail}") #не поняла как решать проблему с появляющимися артефактами
while tail > 0:
    tail *= 10 
    sum += (tail//1)
    tail %= 1
while main > 0:
    sum += main%10
    main //=10
print(f"Сумма цифр числа = {sum}")