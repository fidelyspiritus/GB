from random import choice
coins = [choice(['eagle', 'tail']) for i in range(30)]
print(coins)
count_eagle, count_tails = 0, 0
for coin in coins:
    if coin == 'eagle':
        count_eagle +=1
    else:
        count_tails +=1
if count_eagle > count_tails:
    print(f"Количество монет, которые нужно перевернуть: {count_tails} шт")
else:
    print(f"Количество монет, которые нужно перевернуть: {count_eagle} шт")
