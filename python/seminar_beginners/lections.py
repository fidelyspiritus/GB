from random import randint

def pair(function, array):
    return [function(x) for x in array]

def where (function, array):
    return [x for x in array if function(x)]

n = 15
lst= [randint(0, 79) for _ in range(n)]
print(lst)

# nap = [(i,i**2) for i in lst if i % 2 == 0]
nap = where(lambda x: x % 2 == 0, lst)
print(nap)

res = filter(lambda x: x % 2 == 0, lst)
print(list(res))

res = pair(lambda x: (x, x**2), nap)
print(res)

nap = map(lambda x: (x, x**2), nap)
print(list(nap))

nap = [(i,i**2) for i in lst if i % 2 == 0]
print(nap)