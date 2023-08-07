from random import randint

bush = int(input("Сколько кустов на грядке? "))
berries = int(input("Максимальное количество ягод на одном кусте? "))

garden_bed = [randint(0, berries) for _ in range(bush)]
max_berry = 0

for i in range(bush):
    sum = garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1 - bush]
    if sum > max_berry:
        max_berry = sum
print(f"Всего ягод на кустах {garden_bed}")
print(f"Максимальное число ягод, которое может собрать за один заход собирающий модуль = {max_berry}")