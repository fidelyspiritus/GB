def arifmetics(a, dif, length):
    sequense = [a + n * dif for n in range(length)]
    return sequense

a = int(input("Введите значение первого члена последовательности: "))
dif = int(input("Введите значение шага последовательности: "))
length = int(input("Введите требуемую длину последовательности: "))

print(f'Искомая арифметическая последовательность: {arifmetics(a, dif, length)}')