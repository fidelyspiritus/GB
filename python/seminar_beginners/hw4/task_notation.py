def notation(num, dev):
    number = []
    while num > 0:
        number.append(num % dev)
        num //= dev
    
    result = [str(i) for i in number[::-1]]
    return "".join(result)


num = int(input('Введите число для рассчета: '))
num_binary = notation(num, 2)
num_octal = notation(num, 8)

print(f'Число {num} в двоичном виде равно {num_binary}, проверим? Должно быть {bin(num)}.')
print(f'Число {num} в восьмиричном виде равно {num_octal}, проверим? Должно быть {oct(num)}.')