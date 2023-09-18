from itertools import combinations 

def combine(arr, s): 
    return list(combinations(arr, s)) 

stolen_sum, amount = [int(i) for i in input().split()]
currency = [int(i) for i in input().split()] 
count_currency = -1 
 
for i in range(1,amount*2 +1):
    currency_variation = combine(currency*2, i)
    for var in currency_variation:
        if sum(var) == stolen_sum:
            count_currency = len(var)
            stollen = var

if count_currency == -1:
    print(count_currency)
else:
    print(count_currency) 
    print(" ".join(map(str, stollen)))
