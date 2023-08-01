from random import choice, randint
n = randint(3, 15)
sample = [choice([True, False]) for i in range(n)]
left_part, right_part = sample[0], sample[0]
print(sample)
for i in sample:
  left_part = left_part and i
  right_part = not right_part or not i
print(not left_part == right_part)
