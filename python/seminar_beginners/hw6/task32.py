from random import randint

def index(sequense, min, max):
    minmax_seq = []
    for i in range(len(sequense)):
        if sequense[i] <= max and sequense[i] >= min:
            minmax_seq.append(i)
    return minmax_seq


sequense = [randint(1,240) for _ in range(30)]
min = int(input("Введите начало интересующего вас диапазона: "))
max = int(input("Введите окончание интересующего вас диапазона: "))

print(f"Индексы последовательности, которые попали в нужный диапазон: {index(sequense, min, max)}.")