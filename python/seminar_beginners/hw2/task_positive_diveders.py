number = int(input())
middle = int(number**(1/2)) #можно использовать Math для но не уверена есть ли смысл
pos_div = []
for i in range(1, middle + 1):
  if number % i == 0:
    pos_div.append(i)
    if i != number/i:
      pos_div.append(number//i)
print(sorted(pos_div))
