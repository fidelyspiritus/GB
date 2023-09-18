def first(x, y):
    first_gang = spirits.index([x])
    second_gang = spirits.index([y])
    if first_gang != second_gang:
        for spirit in spirits[first_gang], spirits[second_gang]:
            spirit_gang[spirit] = spirit_gang.get(spirit) + 1

        spirits[first_gang] = [spirits[first_gang], spirits[second_gang]]
        del spirits[second_gang]
    print(spirits)

def second(x, y):
    answer = 'NO'
    for i in spirits:
        if x in i and y in i:
            answer = 'YES'
    print(answer)

def third(x):
    print(spirit_gang[x])

spirit_number, scream = [int(i) for i in input().split()]

spirits = [[i] for i in range(1, spirit_number + 1)]
spirit_gang = {i:1 for i in range(1, spirit_number + 1)}

for _ in range(scream):
    data = [int(i) for i in input().split()]
    print(data)
    if data[0] == 1:
        first(*data[1:])  
    elif data[0] == 2:
        second(*data[1:])
    elif data[0] == 3:
        third(*data[1:])


