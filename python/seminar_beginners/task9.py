number = int(input())
factorial = 1
if number < 1:
    print(factorial)
else:
    while number > 1:
        factorial *= number
        number -=1
    print(factorial)