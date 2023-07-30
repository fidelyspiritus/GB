n = int(input())
temperature = [int(input()) for i in range(n)]
count_day, max_day = 0, 0
for today in temperature:
    if today > 0:
        count_day +=1
    else:
        count_day = 0
    if count_day > max_day:
        max_day = count_day
print(max_day)