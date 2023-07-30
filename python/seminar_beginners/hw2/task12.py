#насколько поняла не надо использовать формулу
#x, y = [int(i) for i in input().split()] 
#sum, pow = x + y, x * y

sum, pow = [int(i) for i in input().split()] 
middle = int(sum/2+1)
for i in range(middle):
    if i * (sum - i) == pow:
        print(f"Петя загадал число {i} и {sum - i}")
        break